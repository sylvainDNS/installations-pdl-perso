from admin.TableAdder import addEquipementsActivites

def equipementActivityImporter(my_cursor, table):
    i = 1 # compteur de ligne
    for ligne in table:
        try:
            addEquipementsActivites(my_cursor, int(ligne[2]), ligne[4])
        except:
            print("Erreur dans activites_table.csv à la ligne " + str(i) + " - ", sys.exc_info()[1])
        i += 1
        # print("equipementActivite_added")
