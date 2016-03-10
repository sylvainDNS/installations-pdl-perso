import sqlite3

def creerTableInstallations(my_cursor):
    # TABLE INSTALLATIONS
    my_cursor.execute('''CREATE TABLE IF NOT EXISTS installations (id INTEGER PRIMARY KEY, nom VARCHAR, adresse VARCHAR, code_postal VARCHAR, ville VARCHAR, latitude DECIMAL, longitude DECIMAL)''')

def creerTableEquipements(my_cursor):
    # TABLE EQUIPEMENTS
    my_cursor.execute('''CREATE TABLE IF NOT EXISTS equipements (id INTEGER PRIMARY KEY, nom VARCHAR, id_installation INTEGER, type VARCHAR, FOREIGN KEY(id_installation) REFERENCES installation(id))''')

def creerTableActivities(my_cursor):
    # TABLE ACTIVITES
    my_cursor.execute('''CREATE TABLE IF NOT EXISTS activites (id INTEGER PRIMARY KEY, nom VARCHAR, id_equipement INTEGER, FOREIGN KEY(id_equipement) REFERENCES equipements(id))''')


def creerTableEquipementsActivities(my_cursor):
    # TABLE EQUIPEMENTS_ACTIVITES
    my_cursor.execute('''CREATE TABLE IF NOT EXISTS equipements_activites (id_equipement INTEGER, id_activite INTEGER, FOREIGN KEY(id_equipement) REFERENCES equipements(id), FOREIGN KEY(id_activite) REFERENCES activites(id), PRIMARY KEY(id_equipement, id_activite))''')
