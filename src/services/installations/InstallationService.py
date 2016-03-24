from services.utils.Utils import queryDb, concat

def queryVille(my_cursor, query):
    # Le % signifie qu'il peut y avoir quelque chose avant/après
    my_query = queryDb(my_cursor, ville(query))

    query = query.replace(" ", "-")
    my_query2 = queryDb(my_cursor, ville(query))

    return concat(my_query, my_query2)

def ville(query):
    return 'SELECT ville, nom FROM installations WHERE ville LIKE ' + '"%' + query + '%" OR lieu_dit LIKE ' + '"%' + query + '%"'
