# -*- coding: utf-8 -*-

"""
    Module InstallationService
    ==========================

    InstallationService formule les requetes effectuees concernant des installations. Il appelle les fonctions du module Utils.

    .. seealso:: Utils.py
"""

from services.utils.Utils import queryDb, concat

def queryVille(my_cursor, query):
    """
        Recherche une ville dans la base de donnees.

        :param my_cursor: Le curseur de connection actuel
        :param query: La ville que l'on recherche
        :type my_cursor: sqlite3.Cursor
        :type query: str

        :return: Le resultat de la requete en fromat Json
        :rtype: str
    """

    # Le % signifie qu'il peut y avoir quelque chose avant/apres
    my_query = queryDb(my_cursor, ville(query))

    query = query.replace(" ", "-")
    my_query2 = queryDb(my_cursor, ville(query))

    return concat(my_query, my_query2)

def ville(query):
    """
        Cree la requete textuelle a effectuer en fonction de la ville recherchee.

        :param query: La ville recherchee
        :type query: str

        :return: La requete a effectuer sur la base de donnees
        :rtype: str
    """

    return 'SELECT ville, nom FROM installations WHERE ville LIKE ' + '"%' + query + '%" OR lieu_dit LIKE ' + '"%' + query + '%"'
