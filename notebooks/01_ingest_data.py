# Databricks notebook source
# ----------------------------------------
# Notebook: 01_ingest_data
# Project: Retail Data Lakehouse
# Purpose:
# Load raw retail data and perform initial profiling.
# ----------------------------------------

df = spark.table("default.online_retail_ii")

# COMMAND ----------

display(df.limit(10))


# COMMAND ----------

df.printSchema()

# COMMAND ----------

print(f"Total Records: {df.count():,}")

# COMMAND ----------

from pyspark.sql.functions import col, count, when

null_counts = df.select([
    count(when(col(c).isNull(), c)).alias(c)
    for c in df.columns
])

display(null_counts)

# COMMAND ----------

# Count duplicate rows
total_rows = df.count()
distinct_rows = df.distinct().count()

print(f"Total Rows    : {total_rows:,}")
print(f"Distinct Rows : {distinct_rows:,}")
print(f"Duplicate Rows: {total_rows - distinct_rows:,}")