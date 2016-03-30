# -*- coding: utf-8 -*-

"""
    Module CSVPusher
    ================

    Le module CSVPusher permet de caster un fichier csv en une liste, tout en supprimant la premiere ligne (entetes).
"""

import csv

def csvPusher(path):
    """
        Caste un fichier csv en une liste et supprime la ligne d'entete.

        :param path: Le chemin d'acces au fichier csv
        :type path: str
    """
    try:
        fichier = open(path, 'r', encoding="utf-8")
        liste = []
        passe = False # pour ne pas prendre la ligne d'entête
        for ligne in csv.reader(fichier):
            if passe == False:
                passe = True
            else:
                for i in range(1,len(ligne)):
                    ligne[i] = ligne[i].replace(' "', '')
                    ligne[i] = ligne[i].replace('"', '')
                liste.append(ligne)
                #print("done")
    finally:
        fichier.close()
        return liste
