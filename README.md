# AWS Airlines Data Pipeline (Glue + Athena)

## Overview
This project implements an end-to-end data pipeline on AWS to process and analyze airline flight data. The pipeline pulls raw datasets from S3 buckets, performs ETL transformations using PySpark, then saves cleaned data back to S3 in a parquet format, and enables SQL-based analytics via AWS Athena.

The goal of this project is to demonstrate how to build end-to-end data pipelines that transform raw data into structured datasets suitable for analysis and decision-making.

---

## Architecture
```
S3 (Raw Data)
   ↓
Glue Crawler → Data Catalog
   ↓
Glue ETL Jobs (PySpark)
   ↓
S3 (Cleaned Parquet Data)
   ↓
Athena (SQL Queries)
```
## Tech Stack
- AWS S3
- AWS Glue (Crawler + ETL Jobs)
- PySpark
- AWS Athena
- Python (pandas for local testing)

## Project Structure
```
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
```
## Key Features
- Built ETL pipeline to clean and transform airline data
- Converted raw CSV data into optimized Parquet format
- Implemented feature engineering:
    - Route (origin → destination)
    - Time-of-day buckets
- Performed deduplication and data validation
- Enabled serverless querying with Athena

## Key Learnings
- Designed an ETL pipeline using AWS tools
- Improved query speed by using columnar storage
- Handled missing values, invalid time ranges, and duplicates
- Combined data engineering and analytics in a cloud environment

## How to run locally
1. Clone the repo

```
git clone https://github.com/zsezim/aws-data-pipeline.git
cd aws-data-pipeline
```
2. Create a virtual environment and activate it (warning: you must use python 3.11 or older!):
```
python3.11 -m venv venv
source venv/bin/activate
```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Run ETL locally:
```
python scripts/local_etl.py
```

## Future improvements
- Add machine learning model for delay prediction
- Implement real-time streaming pipeline (Kafka / Kinesis)
- Deploy pipeline using orchestration tools (Airflow)