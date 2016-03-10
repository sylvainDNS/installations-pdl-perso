from admin.DbAdmin  import *
from admin.TableCreator import *
from importers.utils.CSVPusher import csvPusher
from importers.equipements.EquipementImporter import equipementImporter

def equipements(path):
    conn = db()
    my_cursor = cursor(conn)
    creerTableEquipements(my_cursor)

    equipementTable = csvPusher(path)
    equipementImporter(my_cursor, equipementTable)

    push(conn)
    disconnect(my_cursor)
