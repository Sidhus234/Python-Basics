import sqlite3


class Database:

    def __init__(self, db):
        self.db = db
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()
        pass

    def insert(self, title, author, year, isbn):
        self.cur.execute(
            "INSERT INTO book VALUES (NULL, ? ,?, ?, ?)", (title, author, year, isbn))
        self.conn.commit()
        pass

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute(
            "SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id, ))
        self.conn.commit()
        pass

    def update(self, id, title, author, year, isbn):
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",
                    (title, author, year, isbn, id, ))
        conn.commit()
        pass

    def __del__(self):
        self.conn.close()


#insert("The Seat", "John Tablet", 1918, 232472962)
# print(view())
#insert("Apple", "John Smith", 1987, 354873)
#print(search(author="John Smith"))
# delete(3)
# print(view())
#update(1, "The Moon", "John Tablet", 1918, 232472962)
# print(view())
