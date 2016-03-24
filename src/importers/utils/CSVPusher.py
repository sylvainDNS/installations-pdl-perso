import csv

def csvPusher(path):
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
