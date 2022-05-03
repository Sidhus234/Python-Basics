import sqlite3

# Create a table


def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()
    pass

# Insert item into a table


def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()
    pass

# View rows in a table


def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


# Delete item in a table
def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store where item=?", (item, ))
    conn.commit()
    conn.close()
    pass


# Update data
def update(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? where item=?",
                (quantity, price, item))
    conn.commit()
    conn.close()
    pass


create_table()
insert("Coffee Cup", 10, 5.4)
insert("Tea Pot", 1, 23.4)
insert("Apple", 18, 5.14)
insert("Coffee", 10, 15.4)
delete("Coffee Cup")
print(view())
update("Apple", 20, 4.8)
print(view())
