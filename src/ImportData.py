# -*- coding: utf-8 -*-

"""
    Module ImportData
    =================

    Ce module est l'application qui sert a creer et remplir la base donnees a partir de fichiers csv. Elle ne comporte pas de fonction, mais appelle celles des autres modules de gestion et d'importation de la BD
"""

from importers.installations.Installations import installations
from importers.equipements.Equipements import equipements
from importers.activities.Activities import activities
from importers.equipementsActivities.EquipementsActivities import equipementsActivities

installationsPath = "../csv/installations_table.csv";
equipementsPath = "../csv/equipements_table.csv";
activitiesPath = "../csv/activites_table.csv";

installations(installationsPath);
print("Installations added")
equipements(equipementsPath);
print("Equipements added")
activities(activitiesPath);
print("Activities added")
equipementsActivities(activitiesPath)
print("EquipementsActivities added")
