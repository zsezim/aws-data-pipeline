from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, concat_ws

# Initialize Spark session
spark = SparkSession.builder.appName("AirlinesETL").getOrCreate()

# -----------------------------
# Load Data
# -----------------------------
input_path = "s3://amazing-bucket/raw/airlines/"
output_path = "s3://amazing-bucket/processed/airlines/"

df = spark.read.option("header", "true").csv(input_path)

# -----------------------------
# Data Cleaning
# -----------------------------
df_clean = (
    df
    .dropna(subset=["DEPARTURE_TIME", "ARRIVAL_TIME", "ORIGIN_AIRPORT", "DESTINATION_AIRPORT"])
    .withColumn("DEPARTURE_TIME", col("DEPARTURE_TIME").cast("int"))
    .withColumn("ARRIVAL_TIME", col("ARRIVAL_TIME").cast("int"))
    .withColumn("DEPARTURE_DELAY", col("DEPARTURE_DELAY").cast("double"))
    .filter((col("DEPARTURE_TIME") >= 0) & (col("DEPARTURE_TIME") <= 2359))
)

# -----------------------------
# Feature Engineering
# -----------------------------

# Route column
df_clean = df_clean.withColumn(
    "route",
    concat_ws("_", col("ORIGIN_AIRPORT"), col("DESTINATION_AIRPORT"))
)

# Time-of-day bucket
df_clean = df_clean.withColumn(
    "departure_time_bucket",
    when((col("DEPARTURE_TIME") >= 500) & (col("DEPARTURE_TIME") < 1200), "Morning")
    .when((col("DEPARTURE_TIME") >= 1200) & (col("DEPARTURE_TIME") < 1700), "Afternoon")
    .when((col("DEPARTURE_TIME") >= 1700) & (col("DEPARTURE_TIME") <= 2359), "Evening")
    .when((col("DEPARTURE_TIME") >= 0) & (col("DEPARTURE_TIME") < 500), "Night")
    .otherwise("Unknown")
)

# -----------------------------
# Deduplication
# -----------------------------
df_clean = df_clean.dropDuplicates()

# -----------------------------
# Write Output (Parquet)
# -----------------------------
df_clean.write.mode("overwrite").parquet(output_path)