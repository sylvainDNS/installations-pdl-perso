from admin.TableAdder import addActivites

def activityImporter(my_cursor, table):
    i = 1 # compteur de ligne
    for ligne in table:
        try:
            addActivites(my_cursor, int(ligne[4]), ligne[5], int(ligne[2]))
        except:
            print("Erreur dans activites_table.csv à la ligne " + str(i))
        i += 1
        # print("activite_added")
