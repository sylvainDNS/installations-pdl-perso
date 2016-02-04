# Le composant Import a pour rôle le remplissage des tables de la base de données à partir des fichiers CSV.

import csv
from Admin import *

def BD():
    creerTable()
    importInstallations()
    
def importInstallations():
    fname = "../csv/installations_table.csv"
    fichier = open(fname, 'r')
    
    try:
        lecteur = csv.reader(fichier)

        passe = False
        
        for ligne in lecteur:
            if passe == False:
                passe = True
            else:
                id = int(ligne[1])
                nom = ligne[0]
                adresse = ""
                if ligne[5] != "":
                    adresse += ligne[5] + " "
                if ligne[6] != "":
                    adresse += ligne[6] + " "
                adresse += ligne[7]
                code_postal = ligne[4]
                ville = ligne[2]
                latitude = float(ligne[9])
                longitude = float(ligne[10])
                addInstallations(id, nom, adresse, code_postal, ville, latitude, longitude)
                print("added")
    finally:
        fichier.close()

BD()
