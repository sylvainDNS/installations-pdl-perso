# -*- coding: utf-8 -*-

"""
    Module ActivityImporter
    ===========================

    Ce module traite une liste d'activites et l'ajoute à une base de données.

    .. seealso admin
"""

from admin.TableAdder import addActivites
import sys

def activityImporter(my_cursor, liste):
    """
        Importe une liste d'activites.

        :param my_cursor: Le curseur de connexion actuel
        :param liste: Le liste a importer
        :type my_cursor: sqlite3.Cursor
        :type liste: list
    """

    i = 1 # compteur de ligne
    for ligne in liste:
        try:
            addActivites(my_cursor, int(ligne[4]), ligne[5], int(ligne[2]))
        except:
            print("W! - Erreur dans activites_liste.csv à la ligne " + str(i) + " - ", sys.exc_info()[1])
        i += 1
        # print("activite_added")
