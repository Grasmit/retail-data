# retail-data-pipeline

This pipe line start with extracting data from csv file and ends up in Metabase dashboard

## **Dataset**

https://www.kaggle.com/datasets/tunguz/online-retail

| Column | Description |
| --- | --- |
| InvoiceNo | Invoice number. Nominal, a 6-digit integral number uniquely assigned to each transaction. If this code starts with letter 'c', it indicates a cancellation. |
| StockCode | Product (item) code. Nominal, a 5-digit integral number uniquely assigned to each distinct product. |
| Description | Product (item) name. Nominal. |
| Quantity | The quantities of each product (item) per transaction. Numeric. |
| InvoiceDate | Invice Date and time. Numeric, the day and time when each transaction was generated. |
| UnitPrice | Unit price. Numeric, Product price per unit in sterling. |
| CustomerID | Customer number. Nominal, a 5-digit integral number uniquely assigned to each customer. |
| Country | Country name. Nominal, the name of the country where each customer resides. |

# Pipeline

![Untitled](https://github.com/Grasmit/retail-data/blob/master/images/pipeline.png)

Pipeline include following steps 

- Ingest the raw data to google storage bucket and then into big query
- Run quality check of ingested bigquery schema using Soda
- Building dbt model to transform data
- Running data quality check using Soda
- Building dbt model for report
- Running data quality check using Soda
- Creating dashboard in Metabase

# Data Ingestion

![gcs.png](https://github.com/Grasmit/retail-data/blob/master/images/gcs.png)

![big_query_ingested.png](https://github.com/Grasmit/retail-data/blob/master/images/big_query_ingested.png)

# Data modeling

![Untitled](https://github.com/Grasmit/retail-data/blob/master/images/data_model.png)

Build dbt model to transform the data

![tranformation.png](https://github.com/Grasmit/retail-data/blob/master/images/tranformation.png)

# Final Pipeline

![final_pipeline.png](https://github.com/Grasmit/retail-data/blob/master/images/final_pipeline.png)

# Metabase Dashboard

![dashboard.png](https://github.com/Grasmit/retail-data/blob/master/images/dashboard.png)
