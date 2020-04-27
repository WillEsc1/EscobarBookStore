import sqlite3

def connectToDB():
    # This creates a db called "books.db"
    connection = sqlite3.connect("books.db")

    # The cursor object will allow us to perform SQL commands
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    
    # This will save all the changes that we have made
    connection.commit()

    # This will close the connection
    connection.close()

def Add_Entry(title, author, year, isbn):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    # Using Python string operation makes the program vulnerable to SQL injections
    # ? is the DB-API parameter substitution
    # ? will substitute and we can pass tuple
    cursor.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))

    connection.commit()
    connection.close()

def View_All():
    # This function returns tuples of our book table
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM book")
    tupleAllData = cursor.fetchall()

    connection.close()

    return tupleAllData

def Search_DB(title = "", author = "", year = "", isbn = ""):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?",(title, author, year, isbn))
    tupleAllData = cursor.fetchall()

    connection.close()

    return tupleAllData

def Delete_Entry(id):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM book WHERE id=?", (id,))

    connection.commit()
    connection.close()

def Update_Entry(id, title, author, year, isbn): 
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    cursor.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))

    connection.commit()
    connection.close()

connectToDB()
