# -*- coding: utf-8 -*-

"""
    Module TableCreator
    ===================

    Ce module sert à créer les tables dans la base de données.

    .. seealso:: TableAdder.py, DbAdmin.py
"""

import sqlite3

def addInstallations(my_cursor, id, nom, adresse, code_postal, ville, lieu_dit, latitude, longitude):
    """
        Execute la requete permettant d'ajouter une installation dans la table ``installations``.

        :param my_cursor: Le curseur de connection actuel
        :type my_cursor: sqlite3.Cursor
        :param id: L'id de l'installation
        :param nom: Le nom de l'installation
        :param adresse: L'adresse de l'installation
        :param code_postal: Le code postal de l'installation
        :param ville: La ville de l'installation
        :param lieu_dit: Le lieu dit de l'installation
        :param latitude: La latitude de l'installation
        :param longitude: La longitude de l'installation
        :type id: int
        :type nom: str
        :type adresse: str
        :type code_postal: str
        :type ville: str
        :type lieu_dit: str
        :type latitude: float
        :type longitude: float
    """

    my_cursor.execute('INSERT OR IGNORE INTO installations (id, nom, adresse, code_postal, ville, lieu_dit, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (id, nom, adresse, code_postal, ville, lieu_dit, latitude, longitude))

def addEquipements(my_cursor, id, nom, id_installation, type):
    """
        Execute la requete permettant d'ajouter un équipement dans la table ``equipements``.

        :param my_cursor: Le curseur de connection actuel
        :type my_cursor: sqlite3.Cursor
        :param id: L'id de l'equipement
        :param nom: Le nom de l'equipement
        :param id_installation: L'id de l'installation que possède l'equipement
        :param type: Le type de l'equipement
        :type id: int
        :type nom: str
        :type id_installation: int
        :type type: str
    """

    my_cursor.execute('INSERT OR IGNORE INTO equipements (id, nom, id_installation, type) VALUES (?, ?, ?, ?)', (id, nom, id_installation, type))

def addActivites(my_cursor, id, nom, id_equipement):
    """
        Execute la requete permettant d'ajouter une activité dans la table ``activites``.

        :param my_cursor: Le curseur de connection actuel
        :type my_cursor: sqlite3.Cursor
        :param id: L'id de l'activite
        :param nom: Le nom de l'activite
        :param id_equipement: L'id de l'equipement où se trouve l'installation
        :type id: int
        :type nom: str
        :type id_equipement: int
    """

    my_cursor.execute('INSERT OR IGNORE INTO activites (id, nom, id_equipement) VALUES (?, ?, ?)', (id, nom, id_equipement))

def addEquipementsActivites(my_cursor, id_equipement, id_activite):
    """
        Execute la requete permettant d'ajouter un équipement lié à une activité via leurs id dans la table ``equipementsActivites``.

        :param my_cursor: Le curseur de connection actuel
        :type my_cursor: sqlite3.Cursor
        :param id_equipement: L'id de l'equipement
        :param id_activite: L'id de l'activite
        :type id_equipement: int
        :type id_activite: int
    """
    my_cursor.execute('INSERT OR IGNORE INTO equipements_activites (id_equipement, id_activite) VALUES (?, ?)', (id_equipement, id_activite))
