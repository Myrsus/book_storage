import random
import sqlite3
from collections import namedtuple

conn = sqlite3.connect(r"database.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    author TEXT,
    year INT,
    genre TEXT,
    description TEXT)
""")

GameData = namedtuple('GameData',('id','name','author','year','genre','description'))
def create_game(name,author,year,genre,description):
    cur.execute("INSERT INTO books VALUES(?,?,?,?,?,?)",(None,name,author,year,genre,description))
    conn.commit()

def get_game(id):
    data = cur.execute("SELECT * FROM books WHERE id = ?",(id,)).fetchone()
    if data is None:
        return data
    return GameData(*data)

def search_game(name=None, author=None, year=None, genre = None):
    params = []
    where_clauses = []

    if name:
        where_clauses.append("name = ?")
        params.append(name)
    if author:
        where_clauses.append("author = ?")
        params.append(author)
    if year:
        where_clauses.append("year = ?")
        params.append(year)
    if genre:
        where_clauses.append("genre = ?")
        params.append(genre)

    # Добавляем все условия в запрос, разделяя их ключевым словом AND
    req = "SELECT * FROM books"
    if where_clauses:
        req += " WHERE " + " AND ".join(where_clauses)

    # Выполняем запрос с параметрами
    resp = cur.execute(req, params).fetchall()
    res_list = [GameData(*data) for data in resp] # Парсим каждый котртеж в namedtuple
    return res_list

def update_book_name(id,update):
    cur.execute(f"UPDATE books SET name = ? WHERE id = ?", (update, id))
    conn.commit()
def update_book_author(id,update):
    cur.execute(f"UPDATE books SET author = ? WHERE id = ?", (update, id))
    conn.commit()
def update_book_year(id, update):
    cur.execute(f"UPDATE books SET year = ? WHERE id = ?", (update, id))
    conn.commit()

def update_book_genre(id,update):
    cur.execute(f"UPDATE books SET genre = ? WHERE id = ?", (update, id))
    conn.commit()
def delete_book(id):
    cur.execute("DELETE FROM books WHERE id = ?",(id,))
    conn.commit()