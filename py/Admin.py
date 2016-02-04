# Le composant Admin a pour rôle la création des tables de la base de données.

import sqlite3

def connect():
    conn = sqlite3.connect("/db/myDB.db")
    return conn.cursor()

def disconnect():
    conn.close

def creerTable():
    c = connect()
    c.execute('''CREATE TABLE installations (id INTEGER PRIMARY KEY, nom VARCHAR, adresse VARCHAR, code_postal VARCHAR, ville VARCHAR, latitude DECIMAL, longitude DECIMAL)''')
    c.execute('''CREATE TABLE equipements (id INTEGER PRIMARY KEY, nom VARCHAR, id_installation INTEGER FOREIGN KEY, type VARCHAR)''')
    c.execute('''CREATE TABLE activites (id INTEGER PRIMARY KEY, nom VARCHAR, id_equipement VARCHAR FOREIGN KEY)''')
    c.execute('''CREATE TABLE equipements_activites (id_equipement INTEGER FOREIGN KEY, id_activite INTEGER FOREIGN KEY)''')
    diconnect()

def addInstallations(id, nom, adresse, code_postal, ville, latitude, longitude):
    c = connect()
    c.execute('''INSERT INTO installations (id, nom, adresse, code_postal, ville, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (id, nom, adresse, code_postal, ville, latitude, longitude))
    diconnect()

def addEquipements(id, nom, id_installation, type):
    c = connect()
    c.execute('''INSERT INTO equipements (id, nom, id_installation, type) VALUES (?, ?, ?, ?)''', (id, nom, id_installation, type))
    diconnect()

def addActivites(id, nom, id_equipement):
    c = connect()
    c.execute('''INSERT INTO activites (id, nom, id_equipement) VALUES (?, ?, ?)''', (id, nom, id_equipement))
    diconnect()

def addEquipementsActivites(id_equipement, id_activite):
    c = connect()
    c.execute('''INSERT INTO equipements_activites (id_equipement, id_activite) VALUES (?, ?)''', (id_equipement, id_activite))
    diconnect()
