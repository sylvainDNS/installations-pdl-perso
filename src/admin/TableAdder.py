import sqlite3

def addInstallations(my_cursor, id, nom, adresse, code_postal, ville, lieu_dit, latitude, longitude):
    my_cursor.execute('INSERT OR IGNORE INTO installations (id, nom, adresse, code_postal, ville, lieu_dit, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (id, nom, adresse, code_postal, ville, lieu_dit, latitude, longitude))

def addEquipements(my_cursor, id, nom, id_installation, type):
    my_cursor.execute('INSERT OR IGNORE INTO equipements (id, nom, id_installation, type) VALUES (?, ?, ?, ?)', (id, nom, id_installation, type))

def addActivites(my_cursor, id, nom, id_equipement):
    my_cursor.execute('INSERT OR IGNORE INTO activites (id, nom, id_equipement) VALUES (?, ?, ?)', (id, nom, id_equipement))

def addEquipementsActivites(my_cursor, id_equipement, id_activite):
    my_cursor.execute('INSERT OR IGNORE INTO equipements_activites (id_equipement, id_activite) VALUES (?, ?)', (id_equipement, id_activite))
