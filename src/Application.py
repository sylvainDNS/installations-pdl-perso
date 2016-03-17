from libs.bottle import route, template, run, static_file, error, view
from admin.DbAdmin import db, cursor, disconnect
import json

conn = db()
my_cursor = cursor(conn)

# Définition de la page d'accueil
@route('/')
def index():
    return server_static('index.html')

@route('/activite/<query>')
def activite(query):
    # On reforme la string
    query.replace("%20", " ")
    my_query = query_db('SELECT DISTINCT i.ville FROM installations i JOIN equipements e ON i.id = e.id_installation JOIN equipements_activites ea ON e.id = ea.id_equipement JOIN activites a ON ea.id_activite = a.id WHERE a.nom = ' + '"' + query + '"')
    return my_query

@route('/commune/<query>')
def commune(query):
    my_query = query_db('SELECT nom FROM installations WHERE ville = ' + '"' + query + '"')
    return my_query

# Défintion de la racine du serveur
@route('/<filename>')
def server_static(filename):
    return static_file(filename, root='public')

@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='public')

@error(404)
def error404(error):
    return "La page n'existe pas"

def query_db(query, one=False):
    my_cursor.execute(query)
    result = my_cursor.fetchall()
    disconnect(my_cursor)
    return json.dumps(result)

run(host = 'localhost', port = 8080)
