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
from importers.activities.ActivityImporter import activityImporter

def activities(path):
    """
        Ajoute un fichier csv contenant des activites, dans la base donnees.

        :param path: Le chemin d'acces au fichier csv.
        :type path: str
    """
    conn = db()
    my_cursor = cursor(conn)
    creerTableActivities(my_cursor)

    activityTable = csvPusher(path)
    activityImporter(my_cursor, activityTable)

    push(conn)
    disconnect(my_cursor)
