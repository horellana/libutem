import requests

def login(usuario, contrasena):
    url = 'http://mi.utem.cl/login'
    return requests.post(url, {'usuario': usuario, 'contrasena': contrasena})
    if not r.status_code == requests.codes.ok:
        r.raise_for_status()
    else:
        return r
