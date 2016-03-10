from admin.DbAdmin  import *
from admin.TableCreator import *
from importers.utils.CSVPusher import csvPusher
from importers.installations.InstallationImporter import installationImporter

def installations(path):
    conn = db()
    my_cursor = cursor(conn)
    creerTableInstallations(my_cursor)

    installationTable = csvPusher(path)
    installationImporter(my_cursor, installationTable)

    push(conn)
    disconnect(my_cursor)
