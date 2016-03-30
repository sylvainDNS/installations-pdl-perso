# -*- coding: utf-8 -*-

"""
    Module Equipements
    ================

    Le module Equipements gere et chapeaute l'ajout d'equipements dans la base de donnees.

    .. seealso:: admin.DbAdmin, admin.TableCreator, importers.utils.CSVPusher, importers.equipements.EquipementImporter
"""

from admin.DbAdmin  import *
from admin.TableCreator import *
from importers.utils.CSVPusher import csvPusher
from importers.equipements.EquipementImporter import equipementImporter

def equipements(path):
    """
        Ajoute un fichier csv contenant des equipements, dans la base donnees.

        :param path: Le chemin d'acces au fichier csv.
        :type path: str
    """

    conn = db()
    my_cursor = cursor(conn)
    creerTableEquipements(my_cursor)

    equipementTable = csvPusher(path)
    equipementImporter(my_cursor, equipementTable)

    push(conn)
    disconnect(my_cursor)
