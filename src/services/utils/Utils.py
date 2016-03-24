from admin.DbAdmin import disconnect
import json

def queryDb(my_cursor, query, one=False):
    my_cursor.execute(query)
    result = my_cursor.fetchall()
    disconnect(my_cursor)
    return json.dumps(result)

def concat(my_query, my_query2):
    # On met sous forme de liste
    my_query = eval(my_query)
    my_query2 = eval(my_query2)

    for element in my_query2:
        my_query.append(element)

    return json.dumps(my_query)
