# -*- coding: utf-8 -*-

"""
    Module Utils - The SwissKnife
    =============================

    Le module Utils est le couteau-suisse qui fait le lien entre les requetes specifiques et la base de donnees.
"""

from admin.DbAdmin import disconnect
import json

def queryDb(my_cursor, query, one=False):
    """
        Effectue la requete sur la base de donnees, et renvoie le resultat en format Json.

        :param my_cursor: Le curseur de connection actuel
        :param query: La requete a effectuer
        :type my_cursor: sqlite3.Cursor
        :type query: str

        :return: Le resultat de la requete en format Json
        :rtype: str
    """
    print(type(my_cursor))
    my_cursor.execute(query)
    result = my_cursor.fetchall()
    disconnect(my_cursor)

    return json.dumps(result)


def concat(my_query, my_query2):
    """
        Concatene 2 Json pour n'en former qu'un seul, tout en verifiant les doublons.

        :param my_query: Json numero 1
        :param my_query2: Json numero 2
        :type my_query: str
        :type my_query2: str
        :return: La concatenation des 2 Json
        :rtype: str
    """

    # On met sous forme de liste
    my_query = eval(my_query)
    my_query2 = eval(my_query2)

    for element in my_query2:
        if element not in my_query:
            my_query.append(element)

    return json.dumps(my_query)
