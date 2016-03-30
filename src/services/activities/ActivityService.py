# -*- coding: utf-8 -*-

"""
    Module ActivityService
    ==========================

    ActivityService formule les requetes effectuees concernant des activites. Il appelle les fonctions du module Utils.

    .. seealso:: Utils.py
"""

from services.utils.Utils import queryDb, concat

def queryActivite(my_cursor, query):
    """
        Recherche une activite dans la base de donnees.

        :param my_cursor: Le curseur de connection actuel
        :param query: L'activite que l'on recherche
        :type my_cursor: sqlite3.Cursor
        :type query: str

        :return: Le resultat de la requete en fromat Json
        :rtype: str
    """

    # Le % signifie qu'il peut y avoir quelque chose avant/apres
    my_query = queryDb(my_cursor, activite(query))

    query = query.replace(" ", "-")
    my_query2 = queryDb(my_cursor, activite(query))

    return concat(my_query, my_query2)

def activite(query):
    """
        Cree la requete textuelle a effectuer en fonction de l'activite recherchee.

        :param query: L'activite recherchee
        :type query: str

        :return: La requete a effectuer sur la base de donnees
        :rtype: str
    """

    # Le % signifie qu'il peut y avoir quelque chose avant/apres
    return 'SELECT DISTINCT a.nom, i.ville FROM installations i JOIN equipements e ON i.id = e.id_installation JOIN equipements_activites ea ON e.id = ea.id_equipement JOIN activites a ON ea.id_activite = a.id WHERE a.nom LIKE ' + '"%' + query + '%"'
