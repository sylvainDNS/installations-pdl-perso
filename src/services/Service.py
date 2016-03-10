# Le composant Service a pour rôle d'exposer les fonctionnalités de l'application, au travers de services REST.

from libs.bottle import route, template, run, static_file, error, view
from Admin import *

# psycopg2 ??
conn = db('myDB')
c = cursor(conn)


def query_db(query, one=False):
    conn = db('myDB')
    c = cursor(conn)
    c.execute(query)
    result = c.fetchall()
    disconnect(c)
    return str(result)

@route('/')
def index():
    return server_static('index.html')

@route('/<filename>')
def server_static(filename):
    return static_file(filename, root='../html')

@route('/db/<tablename>')
def getActivites(tablename):
    my_query = query_db('SELECT * FROM ' + tablename)
    return my_query

@route('/show')
def show_picnic():
    conn = db('myDB')
    c = cursor(conn)
    c.execute("SELECT * FROM activites")
    data = c.fetchall()
    disconnect(c)
    output = template('activites', rows=data)
    return output

@error(404)
def error404(error):
    return "La page n'existe pas"

run(host = 'localhost', port = 8080)
