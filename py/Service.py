# Le composant Service a pour rôle d'exposer les fonctionnalités de l'application, au travers de services REST.

from libs.bottle import route, template, run, static_file, error
from Admin import *
import json

# psycopg2 ??

conn = db('myDB')
c = cursor(conn)

def query_db(query, args=(), one=False):
    c.execute(query, args)
    request = [dict((c.description[i][0], value) for i, value in enumerate(row)) for row in c.fetchall()]
    disconnect(c)
    return (request[0] if request else None) if one else request

@route('/')
def index():
    return server_static('index.html')

@route('/<filename>')
def server_static(filename):
    return static_file(filename, root='../html')

@route('/db/activites')
def getActivites():
    my_query = query_db('SELECT * FROM activites', (3,))
    return json.dumps(my_query)

@error(404)
def error404(error):
    return 'Nothing here, sorry'

run(host = 'localhost', port = 8080)
