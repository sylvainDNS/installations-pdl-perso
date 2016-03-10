# Le composant Admin a pour rôle la création des tables de la base de données.
import sqlite3

def db():
    name = 'myDB.db'
    return sqlite3.connect("../db/" + name)

def cursor(conn):
    return conn.cursor()

def push(conn):
    conn.commit()

def disconnect(my_cursor):
    my_cursor.close
