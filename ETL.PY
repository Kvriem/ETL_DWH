import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from DWH_creation import create_dwh_schema
from Generate_dummy_data import create_dummy_data


def extract_data():
    """Extract data from CSV files into DataFrames."""
    author_df = pd.read_csv('author_dim.csv')
    book_df = pd.read_csv('book_dim.csv')
    user_df = pd.read_csv('user_dim.csv')
    date_df = pd.read_csv('date_dim.csv')
    sales_df = pd.read_csv('sales_fact.csv')
    
    return author_df, book_df, user_df, date_df, sales_df

def transform_data(author_df, book_df, user_df, date_df, sales_df):
    """Transform DataFrames to ensure correct data types."""
    
    # Transform author_df
    author_df['author_id'] = author_df['author_id'].astype(int)
    author_df['author_name'] = author_df['author_name'].astype(str)

    # Transform book_df
    book_df['book_id'] = book_df['book_id'].astype(int)
    book_df['book_name'] = book_df['book_name'].astype(str)
    book_df['author_id'] = book_df['author_id'].astype(int)
    book_df['book_price'] = book_df['book_price'].astype(float)

    # Transform user_df
    user_df['user_id'] = user_df['user_id'].astype(int)
    user_df['user_name'] = user_df['user_name'].astype(str)
    user_df['user_email'] = user_df['user_email'].astype(str)

    # Transform date_df
    date_df['date_id'] = date_df['date_id'].astype(int)
    date_df['date'] = pd.to_datetime(date_df['date'])
    date_df['day'] = date_df['date'].dt.day.astype(int)
    date_df['month'] = date_df['date'].dt.month.astype(int)
    date_df['year'] = date_df['date'].dt.year.astype(int)

    # Transform sales_df
    sales_df['sales_id'] = sales_df['sales_id'].astype(int)
    sales_df['book_id'] = sales_df['book_id'].astype(int)
    sales_df['user_id'] = sales_df['user_id'].astype(int)
    sales_df['date_id'] = sales_df['date_id'].astype(int)
    sales_df['sales_amount'] = sales_df['sales_amount'].astype(float)

    return author_df, book_df, user_df, date_df, sales_df

def load_data(author_df, book_df, user_df, date_df, sales_df):


    """Load transformed DataFrames into PostgreSQL tables."""
    engine = create_engine('postgresql://admin:admin@localhost:5433/postgres_DB')

    try:
        author_df.to_sql('author_dim', engine, if_exists='replace', index=False)
        book_df.to_sql('book_dim', engine, if_exists='replace', index=False)
        user_df.to_sql('user_dim', engine, if_exists='replace', index=False)
        date_df.to_sql('date_dim', engine, if_exists='replace', index=False)
        sales_df.to_sql('sales_fact', engine, if_exists='replace', index=False)
        print("Data loaded successfully")
    except Exception as e:
        print(f"Error loading data: {e}")



if __name__ == '__main__':
    create_dwh_schema()
    create_dummy_data()
    author_df, book_df, user_df, date_df, sales_df = extract_data()
    author_df, book_df, user_df, date_df, sales_df = transform_data(author_df, book_df, user_df, date_df, sales_df)
    load_data(author_df, book_df, user_df, date_df, sales_df)