import awswrangler as wr
import pandas as pd
import numpy as np
#import inventory_data, employee_data, sales_data, customer_data, return_data, marketing_data, supply_chain_data, website_traffic_data

sales_data = pd.read_excel("sales_data.xlsx")
inventory_data = pd.read_excel("inventory_data.xlsx")
employee_data = pd.read_excel("employee_data.xlsx")
customer_data = pd.read_excel("customer_data.xlsx")
return_data = pd.read_excel("return_data.xlsx")
marketing_data = pd.read_excel("marketing_data.xlsx")
supply_chain_data = pd.read_excel("supply_chain_data.xlsx")
website_traffic_data = pd.read_excel("website_traffic_data.xlsx")

# Simulating AWS Glue ETL by merging and transforming the datasets

# Extract Phase (Simulating Data Extraction)
sales_df = sales_data.copy()
inventory_df = inventory_data.copy()
customer_df = customer_data.copy()
supply_chain_df = supply_chain_data.copy()
marketing_df = marketing_data.copy()
website_df = website_traffic_data.copy()
return_df = return_data.copy()
employee_df = employee_data.copy()

# Transform Phase
sales_inventory_df = pd.merge(sales_df, inventory_df, on='product_id', how='left')
sales_inventory_df['customer_id'] = np.random.choice(customer_df['customer_id'], len(sales_inventory_df))
sales_customer_df = pd.merge(sales_inventory_df, customer_df, on='customer_id', how='left')
sales_supply_chain_df = pd.merge(sales_customer_df, supply_chain_df, on=['product_id', 'supplier_id'], how='left')
final_df = pd.merge(sales_supply_chain_df, marketing_df, on='product_id', how='left')

final_df['delivery_status'].fillna('Unknown', inplace=True)
final_df['campaign_channel'].fillna('No Campaign', inplace=True)

wr.s3.to_parquet(
    df=final_df,
    path='s3://apparel-data-warehouse/processed/sales_data.parquet',
    dataset=True,
    mode='overwrite'
)

print(final_df.head())