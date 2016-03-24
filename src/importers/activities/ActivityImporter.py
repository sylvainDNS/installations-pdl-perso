from admin.TableAdder import addActivites
import sys

def activityImporter(my_cursor, table):
    i = 1 # compteur de ligne
    for ligne in table:
        try:
            addActivites(my_cursor, int(ligne[4]), ligne[5], int(ligne[2]))
        except:
            print("W! - Erreur dans activites_table.csv à la ligne " + str(i) + " - ", sys.exc_info()[1])
        i += 1
        # print("activite_added")
