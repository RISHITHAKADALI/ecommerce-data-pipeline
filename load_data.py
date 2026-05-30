import pandas as pd
from sqlalchemy import create_engine

# Read CSV file
df = pd.read_csv(r'C:\Users\rishi\Downloads\ecommerce_final_clean.csv')

print("CSV Loaded! Total rows:", len(df))

# Clean data
df = df.where(pd.notnull(df), None)

# Connect to SQL Server
engine = create_engine(
    'mssql+pyodbc://localhost/ecommerce_db?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'
)

# Load into SQL Server
df.to_sql('ecommerce_orders', 
          engine, 
          if_exists='replace', 
          index=False)

print("Data Loaded Successfully! ✅")