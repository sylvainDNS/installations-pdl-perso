from services.utils.Utils import queryDb, concat

def queryActivite(my_cursor, query):
    # Le % signifie qu'il peut y avoir quelque chose avant/après
    my_query = queryDb(my_cursor, activite(query))

    query = query.replace(" ", "-")
    my_query2 = queryDb(my_cursor, activite(query))

    return concat(my_query, my_query2)

def activite(query):
    # Le % signifie qu'il peut y avoir quelque chose avant/après
    return 'SELECT DISTINCT a.nom, i.ville FROM installations i JOIN equipements e ON i.id = e.id_installation JOIN equipements_activites ea ON e.id = ea.id_equipement JOIN activites a ON ea.id_activite = a.id WHERE a.nom LIKE ' + '"%' + query + '%"'
