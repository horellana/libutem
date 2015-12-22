import requests

def login(usuario, contrasena):
    url = 'http://mi.utem.cl/login'
    return requests.post(url, {'usuario': usuario, 'contrasena': contrasena})
