import requests

def login(rut, contrasena):
    url = 'http://mi.utem.cl/login'
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
    r = requests.post(url,
                      data={'rut_alumno': rut, 'contrasena': contrasena},
                      headers={'user-agent': user_agent})

    if not r.status_code == requests.codes.ok:
        r.raise_for_status()
    else:
        return r
