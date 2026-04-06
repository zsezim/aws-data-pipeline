# AWS Airlines Data Pipeline (Glue + Athena)

## Overview
This project implements an end-to-end data pipeline on AWS to process and analyze airline flight data. The pipeline pulls raw datasets from S3 buckets, performs ETL transformations using PySpark, then saves cleaned data back to S3 in a parquet format, and enables SQL-based analytics via AWS Athena.

The goal of this project is to demonstrate how to build end-to-end data pipelines that transform raw data into structured datasets suitable for analysis and decision-making.

---

## Architecture

```mermaid
flowchart TD
    A[S3 Raw Data (CSV Files)] --> B[Glue Crawler]
    B --> C[Glue Data Catalog]
    C --> D[Glue ETL Job (PySpark)]
    D --> E[S3 Processed Data (Parquet)]
    E --> F[AWS Athena]
    F --> G[Analytics / Queries]# aws-data-pipeline
An end-to-end AWS data pipeline using S3, Glue, and Athena to process large-scale airline data, implementing PySpark-based ETL transformations, deduplication, and feature engineering, and enabling serverless querying for analytical insights.

```
## Tech Stack
AWS S3
AWS Glue (Crawler + ETL Jobs)
PySpark
AWS Athena
Python (pandas for local testing)

## Project Structure

aws-airlines-data-pipeline/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── raw/               
│   ├── processed/         
│   └── sample_schema.md    
│
├── scripts/
│   ├── glue_etl_job.py     
│   └── local_etl.py        # Pandas version for local execution
│
├── queries/
│   └── athena_queries.sql
│
├── notebooks/
│   └── analysis.ipynb      # Data exploration
│
└── images/
    └── architecture.png

