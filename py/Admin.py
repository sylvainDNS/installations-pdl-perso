# Le composant Admin a pour rôle la création des tables de la base de données.

import sqlite3
conn = sqlite3.connect("/db/myDB.db")

def connect():
    return conn.cursor()

def disconnect():
    conn.close

def creerTable():
    c = connect()
    c.execute('''CREATE TABLE installation (numero INTEGER PRIMARY KEY, nom TEXT, adresse TEXT, code_postal TEXT, ville TEXT, latitude INTEGER, longitude INTEGER)''')
    c.execute('''CREATE TABLE equipement (numero INTEGER PRIMARY KEY, nom TEXT)''')
    # manque id 
    c.execute('''CREATE TABLE activite (numero INTEGER PRIMARY KEY, nom TEXT)''')
    conn.close

def addInstallation(numero, nom, adresse, code_postal, ville, latitude, longitude):
    c = connect()
    c.execute('''INSERT INTO installation (numero, nom, adresse, code_postal, ville, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (numero, nom, adresse, code_postal, ville, latitude, longitude))
    conn.close

def addEquipement(numero, nom):
    c = connect()
    c.execute('''INSERT INTO equipement (numero, nom) VALUES (?, ?)''', (numero, nom))
    conn.close

def addActivite(numero, nom):
    c = connect()
    c.execute('''INSERT INTO activite (numero, nom) VALUES (?, ?)''', (numero, nom))
    conn.close
