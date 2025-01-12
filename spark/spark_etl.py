from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Apparel ETL") \
    .getOrCreate()

# Read data
df = spark.read.format("csv").option("header", "true").load("data/sales_data.csv")

# Transform: Example - Calculate Total Sales
df = df.withColumn("total_sales", df["quantity"] * df["price_per_unit"])

# Write Transformed Data
df.write.format("parquet").save("data/transformed_sales.parquet")
