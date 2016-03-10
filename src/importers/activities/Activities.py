from admin.DbAdmin  import *
from admin.TableCreator import *
from importers.utils.CSVPusher import csvPusher
from importers.activities.ActivityImporter import activityImporter

def activities(path):
    conn = db()
    my_cursor = cursor(conn)
    creerTableActivities(my_cursor)

    activityTable = csvPusher(path)
    activityImporter(my_cursor, activityTable)

    push(conn)
    disconnect(my_cursor)
