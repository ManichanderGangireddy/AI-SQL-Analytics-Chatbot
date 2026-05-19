import sqlite3
import pandas as pd
conn = sqlite3.connect('enterprise_sales.db')


customers_data = {
   'customer_id': [1, 2, 3, 4],
   'company_name': ['Acme Corp', 'Global Tech', 'Stark Ind', 'Wayne Ent'],
   'region': ['North America', 'Europe', 'North America', 'Asia']
}


sales_data = {
   'order_id': [101, 102, 103, 104, 105],
   'customer_id': [1, 1, 2, 3, 4],
   'product': ['Cloud Hosting', 'Consulting', 'Cloud Hosting', 'Hardware', 'Hardware'],
   'revenue': [5000, 2000, 8500, 12000, 4000],
   'status': ['Completed', 'Completed', 'Pending', 'Completed', 'Cancelled']
}


products_data = {
   'product_name': ['Cloud Hosting', 'Consulting', 'Hardware'],
   'cost_to_build': [2000, 1000, 7000]
}


# Convert to DataFrames
df_customers = pd.DataFrame(customers_data)
df_sales = pd.DataFrame(sales_data)
df_products = pd.DataFrame(products_data)


# Push to DB
df_customers.to_sql('customers', conn, if_exists='replace', index=False)
df_sales.to_sql('sales', conn, if_exists='replace', index=False)
df_products.to_sql('products', conn, if_exists='replace', index=False)


print("✅ Database Ready")


