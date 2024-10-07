import psycopg2
import sys
import pandas as pd

# Database connection parameters
conn_params = {
    'dbname': 'postgres_DB',
    'user': 'admin',
    'password': 'admin',
    'host': 'localhost',
    'port': 5433
}

# Establishing the connection
try:
    conn = psycopg2.connect(**conn_params)
    print("Connection successful")
except Exception as e:
    print(f"Error connecting to the database: {e}")
    sys.exit(1)

cur = conn.cursor()

# Function to create DWH star schema tables
def create_dwh_schema():
    # Create sales fact table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS sales_fact(
        sales_id SERIAL PRIMARY KEY,
        book_id INT,
        user_id INT,
        date_id INT,
        sales_amount FLOAT
    )
    """)
    
    # Create book dimension table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS book_dim(
        book_id SERIAL PRIMARY KEY,
        book_name VARCHAR(255),
        author_id INT,
        book_price FLOAT
    )
    """)
    
    # Create author dimension table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS author_dim(
        author_id SERIAL PRIMARY KEY,
        author_name VARCHAR(255)
    )
    """)
    
    # Create user dimension table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS user_dim(
        user_id SERIAL PRIMARY KEY,
        user_name VARCHAR(255),
        user_email VARCHAR(255)
    )
    """)
    
    # Create date dimension table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS date_dim(
        date_id SERIAL PRIMARY KEY,
        date DATE,
        day INT,
        month INT,
        year INT
    )
    """)
    
    conn.commit()
    print("DWH schema created successfully")



