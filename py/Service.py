# Le composant Service a pour rôle d'exposer les fonctionnalités de l'application, au travers de services REST.

from libs.bottle import route, template, run

@route('/hello/<name>')
def index(name):
    return template('<b>hello {{name}}</b>!', name = name)

run(host = 'localhost', port = 8080)
