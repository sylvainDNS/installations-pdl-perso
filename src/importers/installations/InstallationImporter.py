from admin.TableAdder import addInstallations
import sys

def installationImporter(my_cursor, table):
    i = 1 # compteur de ligne
    for ligne in table:
        try:
            adresse = ""
            if ligne[5] != "":
                adresse += ligne[5] + " "
            if ligne[6] != "":
                adresse += ligne[6] + " "
            adresse += ligne[7]

            lieu_dit = "Non renseigné"
            if(ligne[5] != ""):
                lieu_dit = ligne[5]
            print(lieu_dit)

            addInstallations(my_cursor, int(ligne[1]), ligne[0], adresse, ligne[4], ligne[2], lieu_dit, float(ligne[9]), float(ligne[10]))
        except:
            print("Erreur dans installations_table.csv à la ligne " + str(i) + " - ", sys.exc_info()[1])
        i += 1
        # print("installation_added")
