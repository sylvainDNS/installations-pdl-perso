# -*- coding: utf-8 -*-

"""
    Module Application : le module principal
    ========================================

    Ce module est l'application utilisant bottle.py.
    Toutes les routes sont definies dans ce module.
"""

from libs.bottle import route, template, run, static_file, error, view
from admin.DbAdmin import db, cursor, disconnect
from services.activities.ActivityService import queryActivite
from services.installations.InstallationService import queryVille
import json

conn = db()
my_cursor = cursor(conn)

# Définition de la page d'accueil
@route('/')
def index():
    return server_static('index.html')

@route('/activite/<query>')
def activite(query):
    my_query = queryActivite(my_cursor, query)

    return my_query

@route('/ville/<query>')
def commune(query):
    my_query = queryVille(my_cursor, query)

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

run(host = 'localhost', port = 8080)
