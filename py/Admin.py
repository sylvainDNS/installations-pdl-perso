# Le composant Admin a pour rôle la création des tables de la base de données.
import sqlite3

def db(name):
    name += '.db'
    return sqlite3.connect("../db/" + name)

def cursor(conn):
    return conn.cursor()

def push(conn):
    conn.commit()

def disconnect(c):
    c.close

def creerTable(c):

    # TABLE INSTALLATIONS
    c.execute('''CREATE TABLE IF NOT EXISTS installations (id INTEGER PRIMARY KEY, nom VARCHAR, adresse VARCHAR, code_postal VARCHAR, ville VARCHAR, latitude DECIMAL, longitude DECIMAL)''')

    # TABLE EQUIPEMENTS
    c.execute('''CREATE TABLE IF NOT EXISTS equipements (id INTEGER PRIMARY KEY, nom VARCHAR, id_installation INTEGER, type VARCHAR, FOREIGN KEY(id_installation) REFERENCES installation(id))''')

    # TABLE ACTIVITES
    c.execute('''CREATE TABLE IF NOT EXISTS activites (id INTEGER PRIMARY KEY, nom VARCHAR, id_equipement INTEGER, FOREIGN KEY(id_equipement) REFERENCES equipements(id))''')

    # TABLE EQUIPEMENTS_ACTIVITES
    c.execute('''CREATE TABLE IF NOT EXISTS equipements_activites (id_equipement INTEGER, id_activite INTEGER, FOREIGN KEY(id_equipement) REFERENCES equipements(id), FOREIGN KEY(id_activite) REFERENCES activites(id), PRIMARY KEY(id_equipement, id_activite))''')

def addInstallations(c, id, nom, adresse, code_postal, ville, latitude, longitude):
    c.execute('''INSERT OR IGNORE INTO installations (id, nom, adresse, code_postal, ville, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?)''', (id, nom, adresse, code_postal, ville, latitude, longitude))

def addEquipements(c, id, nom, id_installation, type):
    c.execute('''INSERT OR IGNORE INTO equipements (id, nom, id_installation, type) VALUES (?, ?, ?, ?)''', (id, nom, id_installation, type))

def addActivites(c, id, nom, id_equipement):
    c.execute('''INSERT OR IGNORE INTO activites (id, nom, id_equipement) VALUES (?, ?, ?)''', (id, nom, id_equipement))

def addEquipementsActivites(c, id_equipement, id_activite):
    c.execute('''INSERT OR IGNORE INTO equipements_activites (id_equipement, id_activite) VALUES (?, ?)''', (id_equipement, id_activite))
