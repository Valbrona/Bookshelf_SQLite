import sqlite3

def create_book_table():
    connection = sqlite3.connect("my_app_SQL.db")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS bookshelf(name text primary key, author text, read integer)")

    connection.commit()
    connection.close()

def add_book(name, author):
    books = get_all_books()
    connection = sqlite3.connect("my_app_SQL.db")
    cursor = connection.cursor()

    cursor.execute('INSERT OR REPLACE INTO bookshelf VALUES(?, ?, 0)', (name, author))
    for book in books:
        if name == book["name"] and author == book["author"]:
            print(f"<<{name}>> written by <<{author}>> has already been added yo your list")


    connection.commit()
    connection.close()


def get_all_books():
    connection = sqlite3.connect("my_app_SQL.db")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM bookshelf')
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]

    connection.close()
    return books

def mark_book_as_read(user_input):
    connection = sqlite3.connect("my_app_SQL.db")
    cursor = connection.cursor()

    cursor.execute('UPDATE bookshelf SET read = 1 WHERE name = ?', (user_input,))

    connection.commit()
    connection.close()


def delete_book(user_input):
    connection = sqlite3.connect("my_app_SQL.db")
    cursor = connection.cursor()

    cursor.execute('DELETE FROM bookshelf WHERE name = ?', (user_input,))

    connection.commit()
    connection.close()



