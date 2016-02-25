# Le composant Import a pour rôle le remplissage des tables de la base de données à partir des fichiers CSV.

import csv
import time
from Admin import *

def importer():
    tps1 = time.clock()

    conn = db()
    c = connect(conn)
    creerTable(c)

    # On "règle" les path
    installationCsv = "../csv/installations_table.csv"
    equipementCsv = "../csv/equipements_table.csv"
    activityCsv = "../csv/activites_table.csv"

    # On met les csv dans des tableaux
    installationTable = tablePusher(installationCsv)
    equipementTable = tablePusher(equipementCsv)
    activityTable = tablePusher(activityCsv)

    # On importe dans la BD
    installationDbManager(c, installationTable)
    equipementDbManager(c, equipementTable)
    activityDbManager(c, activityTable)
    equipementActivityDbManager(c, activityTable)

    push(conn)
    disconnect(c)

    tps2 = time.clock()
    print("Temps CPU : " + str(tps2-tps1))

def tablePusher(path):
        try:
            fichier = open(path, 'r', encoding="utf-8")
            table = []
            passe = False # pour ne pas prendre la ligne d'entête
            for ligne in csv.reader(fichier):
                if passe == False:
                    passe = True
                else:
                    table.append(ligne)
                    #print("done")
        finally:
            fichier.close()
            return table

def installationDbManager(c, table):
    i = 1 # compteur de ligne
    for ligne in table:
        try:
            adresse = ""
            if ligne[5] != "":
                adresse += ligne[5] + " "
            if ligne[6] != "":
                adresse += ligne[6] + " "
            adresse += ligne[7]

            addInstallations(c, int(ligne[1]), ligne[0], adresse, ligne[4], ligne[2], float(ligne[9]), float(ligne[10]))
        except:
            print("Erreur dans installations_table.csv à la ligne " + str(i))
        i += 1
        # print("installation_added")

def activityDbManager(c, table):
    i = 1 # compteur de ligne
    for ligne in table:
        try:
            addActivites(c, int(ligne[4]), ligne[5], int(ligne[2]))
        except:
            print("Erreur dans activites_table.csv à la ligne " + str(i))
        i += 1
        # print("activite_added")

def equipementDbManager(c, table):
    i = 1 # compteur de ligne
    for ligne in table:
        try:
            addEquipements(c, int(ligne[4]), ligne[5], int(ligne[2]), ligne[7])
        except:
            print("Erreur dans equipement_table.csv à la ligne " + str(i))
        i += 1
        # print("equipement_added")

def equipementActivityDbManager(c, table):
    i = 1 # compteur de ligne
    for ligne in table:
        try:
            addEquipementsActivites(c, int(ligne[2]), ligne[4])
        except:
            print("Erreur dans activites_table.csv à la ligne " + str(i))
        i += 1
        # print("equipementActivite_added")

importer()
