import csv

def csvPusher(path):
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
