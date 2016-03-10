from admin.TableAdder import addEquipements

def equipementImporter(my_cursor, table):
    i = 1 # compteur de ligne
    for ligne in table:
        try:
            addEquipements(my_cursor, int(ligne[4]), ligne[5], int(ligne[2]), ligne[7])
        except:
            print("Erreur dans equipement_table.csv à la ligne " + str(i))
        i += 1
        # print("equipement_added")
