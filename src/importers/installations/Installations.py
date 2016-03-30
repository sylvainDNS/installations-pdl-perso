# -*- coding: utf-8 -*-

"""
    Module Installations
    ================

    Le module Installations gere et chapeaute l'ajout d'installations dans la base de donnees.

    .. seealso:: admin.DbAdmin, admin.TableCreator, importers.utils.CSVPusher, importers.installations.InstallationImporter
"""

from admin.DbAdmin  import *
from admin.TableCreator import *
from importers.utils.CSVPusher import csvPusher
from importers.installations.InstallationImporter import installationImporter

def installations(path):
    """
        Ajoute un fichier csv contenant des installations, dans la base donnees.

        :param path: Le chemin d'acces au fichier csv.
        :type path: str
    """

    conn = db()
    my_cursor = cursor(conn)
    creerTableInstallations(my_cursor)

    installationTable = csvPusher(path)
    installationImporter(my_cursor, installationTable)

    push(conn)
    disconnect(my_cursor)
