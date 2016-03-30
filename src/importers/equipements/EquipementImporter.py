# -*- coding: utf-8 -*-

"""
    Module EquipementImporter
    ===========================

    Ce module traite une liste d'equipements et l'ajoute à une base de donnees.

    .. seealso admin
"""

from admin.TableAdder import addEquipements

def equipementImporter(my_cursor, liste):
    """
        Importe une liste d'equipements.

        :param my_cursor: Le curseur de connexion actuel
        :param liste: Le liste a importer
        :type my_cursor: sqlite3.Cursor
        :type liste: list
    """

    i = 1 # compteur de ligne
    for ligne in liste:
        try:
            addEquipements(my_cursor, int(ligne[4]), ligne[5], int(ligne[2]), ligne[7])
        except:
            print("Erreur dans equipement_liste.csv à la ligne " + str(i) + " - ", sys.exc_info()[1])
        i += 1
        # print("equipement_added")
