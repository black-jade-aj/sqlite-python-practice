import csv
import sqlite3

#1 Create a connection to the SQLite database
conn = sqlite3.connect("store.db")
cursor = conn.cursor()

#2 Create a the customers table
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
     customer_id INTEGER PRIMARY KEY,
     first_name TEXT,
        last_name TEXT,
        email TEXT,
        city TEXT,
        join_date TEXT
)''')

#3 import data from the CSV file into the customers table
with open("customers.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    cursor.executemany("INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?)", reader)

#Create the orders table
cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
     order_id INTEGER PRIMARY KEY,
     customer_id INTEGER,
     product_name TEXT,
     category TEXT,
     quantity INTEGER,
     unit_price REAL,
     order_date TEXT
)''')

# Import data from the CSV file into the orders table
with open("orders.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    cursor.executemany("INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?, ?)", reader)   

    # Commit the changes and close the connection
conn.commit()
print("Database setup complete and data imported successfully.")
conn.close()
