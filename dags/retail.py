from airflow.decorators import dag,task
from datetime import datetime,timedelta

from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator

from astro import sql as aql
from astro.files import File
from astro.sql.table import Table, Metadata
from astro.constants import FileType

from include.dbt.cosmos_config import DBT_PROJECT_CONFIG, DBT_CONFIG
from cosmos.airflow.task_group import DbtTaskGroup
from cosmos.constants import LoadMode
from cosmos.config import ProjectConfig, RenderConfig
from airflow.models.baseoperator import chain

default_args = {
    'execution_timeout': timedelta(hours=2),  # Set execution timeout to 30 minutes
    # Other default arguments...
}

@dag(

    start_date=datetime(2023,1,1),
    schedule=None,
    catchup=False,
    default_args=default_args,
    tags=['retail']
)

def retail():

    upload_csv_to_gcs = LocalFilesystemToGCSOperator(

        task_id="upload_csv_to_gcs",
        src="include/dataset/Online_Retail.csv",
        dst="raw/online_retail.csv",
        bucket="dp_online_retail",
        gcp_conn_id="gcp",
        mime_type="text/csv",
    )

    create_retail_dataset = BigQueryCreateEmptyDatasetOperator(
        task_id="create_retail_dataset",
        dataset_id="retail",
        gcp_conn_id="gcp"
    )

    gcp_to_raw = aql.load_file(

        task_id="gcp_to_raw",
        input_file=File(
            'gs://dp_online_retail/Online_Retail.csv',
            conn_id="gcp",
            filetype=FileType.CSV,
        ),
        output_table=Table(
            name="raw_invoices",
            conn_id="gcp",
            metadata=Metadata(schema='retail')
        ),
        use_native_support=False
    )

    @task.external_python(python='/usr/local/airflow/soda_venv/bin/python')
    def check_load(scan_name='check_load', checks_subpath='sources'):
        from include.soda.check_function import check

        return check(scan_name, checks_subpath)

    transform = DbtTaskGroup(
        group_id='transform',
        project_config=DBT_PROJECT_CONFIG,
        profile_config=DBT_CONFIG,
        render_config=RenderConfig(
            load_method=LoadMode.DBT_LS,
            select=['path:models/transform']
        )
    )

    @task.external_python(python='/usr/local/airflow/soda_venv/bin/python')
    def check_transform(scan_name='check_transform', checks_subpath='transform'):
        from include.soda.check_function import check

        return check(scan_name, checks_subpath)

    report = DbtTaskGroup(
        group_id='report',
        project_config=DBT_PROJECT_CONFIG,
        profile_config=DBT_CONFIG,
        render_config=RenderConfig(
            load_method=LoadMode.DBT_LS,
            select=['path:models/report']
        )
    )

    @task.external_python(python='/usr/local/airflow/soda_venv/bin/python')
    def check_report(scan_name='check_report', checks_subpath='report'):
        from include.soda.check_function import check

        return check(scan_name, checks_subpath)

    chain(
        upload_csv_to_gcs,
        create_retail_dataset,
        gcp_to_raw,
        check_load(),
        transform,
        check_transform(),
        report,
        check_report()
    )

retail()