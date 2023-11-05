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

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/38742935-7215-491c-ba2e-cf11716bbce7/344ba11b-50ae-4a6c-92ab-3cf8cd1c4490/Untitled.png)

Pipeline include following steps 

- Ingest the raw data to google storage bucket and then into big query
- Run quality check of ingested bigquery schema using Soda
- Building dbt model to transform data
- Running data quality check using Soda
- Building dbt model for report
- Running data quality check using Soda
- Creating dashboard in Metabase

# Data Ingestion

![gcs.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/38742935-7215-491c-ba2e-cf11716bbce7/55eb5d18-0a24-40d0-8806-48669a309e6d/gcs.png)

![big_query_ingested.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/38742935-7215-491c-ba2e-cf11716bbce7/62c79fa0-8fbc-4939-b069-1b35b5545c4d/big_query_ingested.png)

# Data modeling

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/38742935-7215-491c-ba2e-cf11716bbce7/3e384b7a-a141-40ba-99b7-390fe8be7ef3/Untitled.png)

Build dbt model to transform the data

![tranformation.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/38742935-7215-491c-ba2e-cf11716bbce7/d9294aaa-a57a-4139-8941-18b33ba8a8cb/tranformation.png)

# Final Pipeline

![final_pipeline.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/38742935-7215-491c-ba2e-cf11716bbce7/78c10b9d-8b21-470d-acef-948c333b9e85/final_pipeline.png)

# Metabase Dashboard

![dashboard.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/38742935-7215-491c-ba2e-cf11716bbce7/d1236499-f925-436d-b038-1b0377f58e5e/dashboard.png)
