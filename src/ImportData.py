from importers.installations.Installations import installations
from importers.equipements.Equipements import equipements
from importers.activities.Activities import activities
from importers.equipementsActivities.EquipementsActivities import equipementsActivities

installationsPath = "../csv/installations_table.csv";
equipementsPath = "../csv/equipements_table.csv";
activitiesPath = "../csv/activites_table.csv";

installations(installationsPath);
equipements(equipementsPath);
activities(activitiesPath);
equipementsActivities(activitiesPath)
