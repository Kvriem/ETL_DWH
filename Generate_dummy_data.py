import random
import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker()

def create_dummy_data(num_records=100):
    # Create author dimension data
    authors = []
    for _ in range(10):  # Create 10 authors
        author_name = fake.name()
        authors.append({"author_id": len(authors) + 1, "author_name": author_name})
    
    # Create book dimension data
    books = []
    for _ in range(20):  # Create 20 books
        book_name = fake.catch_phrase()
        author_id = random.choice(authors)["author_id"]
        book_price = round(random.uniform(5.0, 50.0), 2)
        books.append({"book_id": len(books) + 1, "book_name": book_name, "author_id": author_id, "book_price": book_price})
    
    # Create user dimension data
    users = []
    for _ in range(15):  # Create 15 users
        user_name = fake.name()
        user_email = fake.email()
        users.append({"user_id": len(users) + 1, "user_name": user_name, "user_email": user_email})
    
    # Create date dimension data
    dates = []
    for day in range(1, 31):  # For simplicity, only use one month
        date = f"2024-10-{day:02d}"
        dates.append({"date_id": day, "date": date, "day": day, "month": 10, "year": 2024})
    
    # Create sales fact table data
    sales = []
    for _ in range(num_records):
        book_id = random.randint(1, len(books))
        user_id = random.randint(1, len(users))
        date_id = random.randint(1, 30)  # Assuming you have 30 dates in the date_dim
        sales_amount = round(random.uniform(10.0, 100.0), 2)
        sales.append({"sales_id": len(sales) + 1, "book_id": book_id, "user_id": user_id, "date_id": date_id, "sales_amount": sales_amount})
    
    # Convert data to DataFrames
    authors_df = pd.DataFrame(authors)
    books_df = pd.DataFrame(books)
    users_df = pd.DataFrame(users)
    dates_df = pd.DataFrame(dates)
    sales_df = pd.DataFrame(sales)

    # Save DataFrames to CSV files
    authors_df.to_csv('author_dim.csv', index=False)
    books_df.to_csv('book_dim.csv', index=False)
    users_df.to_csv('user_dim.csv', index=False)
    dates_df.to_csv('date_dim.csv', index=False)
    sales_df.to_csv('sales_fact.csv', index=False)

    print("Dummy data created and exported to CSV files successfully.")

