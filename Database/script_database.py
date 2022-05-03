import sqlite3

# Create a connection
# If database exit, it connects to it. If not, it creates a database
conn = sqlite3.connect("lite.db")
# Refer cursor to the connection
cur = conn.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
# Add data to the table
cur.execute("INSERT INTO store VALUES ('WINE GLASS', 8, 10.5)")
conn.commit()
conn.close()
