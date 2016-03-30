# -*- coding: utf-8 -*-

"""
    Module EquipementActivityImporter
    ===========================

    Ce module traite une liste d'equipements/activites et l'ajoute à une base de donnees.

    .. seealso admin
"""

from admin.TableAdder import addEquipementsActivites

def equipementActivityImporter(my_cursor, liste):
    """
        Importe une liste d'equipements/activites.

        :param my_cursor: Le curseur de connexion actuel
        :param liste: Le liste a importer
        :type my_cursor: sqlite3.Cursor
        :type liste: list
    """

    i = 1 # compteur de ligne
    for ligne in liste:
        try:
            addEquipementsActivites(my_cursor, int(ligne[2]), ligne[4])
        except:
            print("Erreur dans activites_liste.csv à la ligne " + str(i) + " - ", sys.exc_info()[1])
        i += 1
        # print("equipementActivite_added")
