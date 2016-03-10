from admin.DbAdmin  import *
from admin.TableCreator import *
from importers.utils.CSVPusher import csvPusher
from importers.equipementsActivities.EquipementActivityImporter import equipementActivityImporter

def equipementsActivities(path):
    conn = db()
    my_cursor = cursor(conn)
    creerTableEquipementsActivities(my_cursor)

    equipementActivityTable = csvPusher(path)
    equipementActivityImporter(my_cursor, equipementActivityTable)

    push(conn)
    disconnect(my_cursor)
