# Le composant Import a pour rôle le remplissage des tables de la base de données à partir des fichiers CSV.

import csv
import time
from Admin import *

def BD():
    tps1 = time.clock()
    creerTable()
    importInstallations()
    importEquipements()
    importActivites()
    tps2 = time.clock()
    print("Temps CPU : " + str(tps2-tps1))

def importInstallations():
    fname = "../csv/installations_table.csv"
    fichier = open(fname, 'r', encoding="utf-8")

    try:
        lecteur = csv.reader(fichier)

        passe = False

        i = 1

        for ligne in lecteur:
            if passe == False:
                passe = True
            else:
                try:
                    adresse = ""
                    if ligne[5] != "":
                        adresse += ligne[5] + " "
                    if ligne[6] != "":
                        adresse += ligne[6] + " "
                    adresse += ligne[7]

                    addInstallations(int(ligne[1]), ligne[0], adresse, ligne[4], ligne[2], float(ligne[9]), float(ligne[10]))
                except:
                    print("Erreur dans le CSV à la ligne " + str(i))
                i += 1
    finally:
        fichier.close()
    print("installation_added")

def importEquipements():
    fname = "../csv/equipements_table.csv"
    fichier = open(fname, 'r')

    try:
        lecteur = csv.reader(fichier)

        passe = False

        i = 1

        for ligne in lecteur:
            if passe == False:
                passe = True
            else:
                try:
                    addEquipements(int(ligne[4]), ligne[5], int(ligne[2]), ligne[7])
                except:
                    print("Erreur dans le CSV à la ligne " + str(i))
                i += 1
    finally:
        fichier.close()
    print("equipement_added")

def importActivites():
    fname = "../csv/activites_table.csv"
    fichier = open(fname, 'r')

    try:
        lecteur = csv.reader(fichier)

        passe = False

        i = 1

        for ligne in lecteur:
            if passe == False:
                passe = True
            else:
                try:
                    addActivites(int(ligne[4]), ligne[5], int(ligne[2]))
                except:
                    print("Erreur dans le CSV à la ligne " + str(i))
                i += 1
    finally:
        fichier.close()
    print("activite_added")

def defEquipementsActivites():
    return -1

BD()
