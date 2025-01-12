import os
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
from spark.spark_etl import spark_etl
from ml.train_model import train_forecasting_model
from monitoring.prometheus_setup import start_prometheus_monitoring

# Define file paths
BASE_DIR = r"C:\\Users\\zenit\\OneDrive\\Desktop\\Course materials\\Projects\\Apparel Infosys"
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# Step 1: ETL Pipeline
def run_etl():
    print("Running ETL Pipeline...")
    sales_file = os.path.join(DATA_DIR, "sales_data.xlsx")
    transformed_file = os.path.join(OUTPUT_DIR, "transformed_sales.csv")
    
    # Extract
    sales_data = extract_data(sales_file)
    
    # Transform
    transformed_data = transform_data(sales_data)
    
    # Load
    load_data(transformed_data, transformed_file)

# Step 2: Spark Transformations
def run_spark():
    print("Running Spark Transformations...")
    transformed_file = os.path.join(OUTPUT_DIR, "transformed_sales.csv")
    spark_output = os.path.join(OUTPUT_DIR, "spark_output.parquet")
    spark_transformations(transformed_file, spark_output)

# Step 3: ML Model Training
def run_ml():
    print("Running Machine Learning Training...")
    train_forecasting_model()

# Step 4: Monitoring with Prometheus and Grafana
def run_monitoring():
    print("Starting Prometheus Monitoring...")
    start_prometheus_monitoring()

# Main Execution
if __name__ == "__main__":
    print("Starting 'Apparel Infosys' Project Workflow...")
    
    # Step 1: Run ETL
    run_etl()
    
    # Step 2: Run Spark
    run_spark()
    
    # Step 3: Train ML Models
    run_ml()
    
    # Step 4: Start Monitoring
    run_monitoring()
    
    print("All tasks completed successfully!")
