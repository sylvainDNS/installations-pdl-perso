# -*- coding: utf-8 -*-

"""
    Module TableCreator
    ===================

    Ce module sert a creer les tables dans la base de donnees.

    .. seealso:: TableAdder.py, DbAdmin.py
"""

import sqlite3

def creerTableInstallations(my_cursor):
    """
        Execute la requête permettant de créer la table ``installations``.

        :param my_cursor: Le curseur de connexion actuel
        :type my_cursor: sqlite3.Cursor
    """

    # TABLE INSTALLATIONS
    my_cursor.execute('''CREATE TABLE IF NOT EXISTS installations (id INTEGER PRIMARY KEY, nom VARCHAR, adresse VARCHAR, code_postal VARCHAR, ville VARCHAR, lieu_dit VARCHAR, latitude DECIMAL, longitude DECIMAL)''')

def creerTableEquipements(my_cursor):
    """
        Execute la requête permettant de créer la table ``equipements``.

        :param my_cursor: Le curseur de connexion actuel
        :type my_cursor: sqlite3.Cursor
    """

    # TABLE EQUIPEMENTS
    my_cursor.execute('''CREATE TABLE IF NOT EXISTS equipements (id INTEGER PRIMARY KEY, nom VARCHAR, id_installation INTEGER, type VARCHAR, FOREIGN KEY(id_installation) REFERENCES installations(id))''')

def creerTableActivities(my_cursor):
    """
        Execute la requête permettant de créer la table ``activites``.

        :param my_cursor: Le curseur de connexion actuel
        :type my_cursor: sqlite3.Cursor
    """

    # TABLE ACTIVITES
    my_cursor.execute('''CREATE TABLE IF NOT EXISTS activites (id INTEGER PRIMARY KEY, nom VARCHAR, id_equipement INTEGER, FOREIGN KEY(id_equipement) REFERENCES equipements(id))''')


def creerTableEquipementsActivities(my_cursor):
    """
        Execute la requête permettant de créer la table ``equipementsActivites``.

        :param my_cursor: Le curseur de connexion actuel
        :type my_cursor: sqlite3.Cursor
    """

    # TABLE EQUIPEMENTS_ACTIVITES
    my_cursor.execute('''CREATE TABLE IF NOT EXISTS equipements_activites (id_equipement INTEGER, id_activite INTEGER, FOREIGN KEY(id_equipement) REFERENCES equipements(id), FOREIGN KEY(id_activite) REFERENCES activites(id), PRIMARY KEY(id_equipement, id_activite))''')
