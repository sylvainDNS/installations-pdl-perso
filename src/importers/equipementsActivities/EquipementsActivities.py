# -*- coding: utf-8 -*-

"""
    Module EquipementsActivities
    ================

    Le module EquipementsActivities gere et chapeaute l'ajout d'equipements/activites dans la base de donnees.

    .. seealso:: admin.DbAdmin, admin.TableCreator, importers.utils.CSVPusher, importers.equipementsActivities.EquipementActivityImporter
"""

from admin.DbAdmin  import *
from admin.TableCreator import *
from importers.utils.CSVPusher import csvPusher
from importers.equipementsActivities.EquipementActivityImporter import equipementActivityImporter

def equipementsActivities(path):
    """
        Ajoute un fichier csv contenant des equipements/activites, dans la base donnees.

        :param path: Le chemin d'acces au fichier csv.
        :type path: str
    """

    conn = db()
    my_cursor = cursor(conn)
    creerTableEquipementsActivities(my_cursor)

    equipementActivityTable = csvPusher(path)
    equipementActivityImporter(my_cursor, equipementActivityTable)

    push(conn)
    disconnect(my_cursor)
