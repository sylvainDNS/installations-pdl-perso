# -*- coding: utf-8 -*-

"""
    Module DbAdmin
    ==============

    DbAdmin sert a administrer la base de donnees.

    .. seealso:: TableAdder.py, DbAdmin.py
"""

import sqlite3

def db():
    """
        Se connecte a la base de donnees myDB.db

        :return: La connexion a la base de donnees
        :rtype: sqlite3.Connection
    """

    name = 'myDB.db'
    return sqlite3.connect("../db/" + name)

def cursor(conn):
    """
        Renvoie le curseur de connexion.

        :return: Le curseur de connexion
        :rtype: sqlite3.Cursor
    """

    return conn.cursor()

def push(conn):
    """
        Effectue un commit sur la base de donnees.

        :param conn: La connexion a la base de donnees
        :type conn: sqlite3.Connection
    """

    conn.commit()

def disconnect(my_cursor):
    """
        Permet de se deconnecter de la base de donnees.

        :param my_cursor: Le curseur de connexion actuel
        :type my_cursor: sqlite3.Cursor
    """

    my_cursor.close
