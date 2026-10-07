import sqlite3
conn = sqlite3.connect('store.db')
cursor = conn.cursor()

query = """
SELECT product_name, unit_price, quantity
FROM orders
WHERE category = 'Electronics'"""

cursor.execute(query)
results = cursor.fetchall()

print("--- Electronics Orders ---")
for row in results:
    print(f"Product: {row[0]}, unit price: {row[1]}, Quantity: {row[2]}")

conn.close()
