import awswrangler as wr
import pandas as pd
import numpy as np

# Generate Fake Datasets
np.random.seed(42)

# Sales Data
sales_data = pd.DataFrame({
    'transaction_id': np.arange(10001, 10101),
    'store_id': np.random.randint(1, 11, 100),
    'product_id': np.random.randint(101, 201, 100),
    'quantity': np.random.randint(1, 5, 100),
    'price_per_unit': np.random.uniform(10, 200, 100).round(2),
    'transaction_date': pd.date_range(start='2024-01-01', periods=100, freq='D')
})
sales_data['total_amount'] = sales_data['quantity'] * sales_data['price_per_unit']

# Inventory Data
inventory_data = pd.DataFrame({
    'product_id': np.arange(101, 201),
    'product_name': [f'Product_{i}' for i in range(101, 201)],
    'category': np.random.choice(['Tops', 'Bottoms', 'Shoes', 'Accessories'], 100),
    'stock_level': np.random.randint(10, 200, 100),
    'reorder_point': np.random.randint(5, 50, 100),
    'supplier_id': np.random.randint(201, 301, 100)
})

# Customer Data
customer_data = pd.DataFrame({
    'customer_id': np.arange(5001, 5101),
    'name': [f'Customer_{i}' for i in range(5001, 5101)],
    'age': np.random.randint(18, 65, 100),
    'gender': np.random.choice(['M', 'F'], 100),
    'total_spent': np.random.uniform(100, 5000, 100).round(2),
    'loyalty_score': np.random.randint(1, 100, 100),
    'purchase_frequency': np.random.randint(1, 12, 100)
})

# Supply Chain Data
supply_chain_data = pd.DataFrame({
    'shipment_id': np.arange(4001, 4101),
    'supplier_id': np.random.randint(201, 301, 100),
    'product_id': np.random.randint(101, 201, 100),
    'quantity_shipped': np.random.randint(20, 500, 100),
    'shipment_date': pd.date_range(start='2024-01-01', periods=100, freq='5D'),
    'delivery_status': np.random.choice(['On Time', 'Delayed'], 100)
})

# Marketing Campaign Data
marketing_data = pd.DataFrame({
    'campaign_id': np.arange(7001, 7101),
    'product_id': np.random.randint(101, 201, 100),
    'campaign_channel': np.random.choice(['Email', 'Social Media', 'TV', 'Billboard'], 100),
    'budget': np.random.uniform(5000, 50000, 100).round(2),
    'start_date': pd.date_range(start='2024-02-01', periods=100, freq='7D'),
    'end_date': pd.date_range(start='2024-03-01', periods=100, freq='7D')
})

# Additional Datasets

# Website Traffic Data
website_traffic_data = pd.DataFrame({
    'visitor_id': np.arange(9001, 9101),
    'session_id': np.arange(10001, 10101),
    'visit_date': pd.date_range(start='2024-01-01', periods=100, freq='D'),
    'page_views': np.random.randint(1, 15, 100),
    'time_spent': np.random.uniform(2, 30, 100).round(2),
    'referral_source': np.random.choice(['Google', 'Facebook', 'Direct'], 100)
})

# Return and Refund Data
return_data = pd.DataFrame({
    'return_id': np.arange(11001, 11101),
    'transaction_id': np.random.choice(sales_data['transaction_id'], 100),
    'product_id': np.random.randint(101, 201, 100),
    'return_reason': np.random.choice(['Damaged', 'Wrong Size', 'Other'], 100),
    'refund_amount': np.random.uniform(10, 200, 100).round(2),
    'return_date': pd.date_range(start='2024-03-01', periods=100, freq='D')
})

# Employee Data
employee_data = pd.DataFrame({
    'employee_id': np.arange(8001, 8101),
    'department': np.random.choice(['Sales', 'Marketing', 'Logistics'], 100),
    'role': np.random.choice(['Manager', 'Analyst', 'Associate'], 100),
    'salary': np.random.randint(40000, 100000, 100),
    'hire_date': pd.date_range(start='2020-01-01', periods=100, freq='30D')
})

# Save to Excel
sales_data.to_excel('sales_data.xlsx', index=False)
inventory_data.to_excel('inventory_data.xlsx', index=False)
customer_data.to_excel('customer_data.xlsx', index=False)
supply_chain_data.to_excel('supply_chain_data.xlsx', index=False)
marketing_data.to_excel('marketing_data.xlsx', index=False)
website_traffic_data.to_excel('website_traffic_data.xlsx', index=False)
return_data.to_excel('return_data.xlsx', index=False)
employee_data.to_excel('employee_data.xlsx', index=False)
