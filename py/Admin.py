# Le composant Admin a pour rôle la création des tables de la base de données.

import sqlite3

def connect():
    conn = sqlite3.connect("../db/myDB.db")
    return conn.cursor()

def disconnect(c):
    c.close

def creerTable():
    c = connect()

    # TABLE INSTALLATIONS
    c.execute('''CREATE TABLE IF NOT EXISTS installations (id INTEGER PRIMARY KEY, nom VARCHAR, adresse VARCHAR, code_postal VARCHAR, ville VARCHAR, latitude DECIMAL, longitude DECIMAL)''')

    # TABLE EQUIPEMENTS
    c.execute('''CREATE TABLE IF NOT EXISTS equipements (id INTEGER PRIMARY KEY, nom VARCHAR, id_installation INTEGER, type VARCHAR, FOREIGN KEY(id_installation) REFERENCES installation(id))''')

    # TABLE ACTIVITES
    c.execute('''CREATE TABLE IF NOT EXISTS activites (id INTEGER PRIMARY KEY, nom VARCHAR, id_equipement VARCHAR, FOREIGN KEY(id_equipement) REFERENCES equipements(id))''')

    # TABLE EQUIPEMENTS_ACTIVITES
    c.execute('''CREATE TABLE IF NOT EXISTS equipements_activites (id_equipement INTEGER, id_activite INTEGER, FOREIGN KEY(id_equipement) REFERENCES equipements(id), FOREIGN KEY(id_activite) REFERENCES activites(id), PRIMARY KEY(id_equipement, id_activite))''')

    disconnect(c)

def addInstallations(id, nom, adresse, code_postal, ville, latitude, longitude):
    c = connect()
    c.execute('''INSERT INTO installations (id, nom, adresse, code_postal, ville, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?)''', (id, nom, adresse, code_postal, ville, latitude, longitude))
    disconnect(c)

def addEquipements(id, nom, id_installation, type):
    c = connect()
    c.execute('''INSERT INTO equipements (id, nom, id_installation, type) VALUES (?, ?, ?, ?)''', (id, nom, id_installation, type))
    disconnect(c)

def addActivites(id, nom, id_equipement):
    c = connect()
    c.execute('''INSERT INTO activites (id, nom, id_equipement) VALUES (?, ?, ?)''', (id, nom, id_equipement))
    disconnect(c)

def addEquipementsActivites(id_equipement, id_activite):
    c = connect()
    c.execute('''INSERT INTO equipements_activites (id_equipement, id_activite) VALUES (?, ?)''', (id_equipement, id_activite))
    disconnect(c)
