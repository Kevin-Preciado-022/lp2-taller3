"""
Cliente HTTP hacia el servicio 'api'.

Este módulo concentra TODAS las llamadas de red hacia la API, para que
routes.py no tenga que preocuparse por URLs, timeouts o códigos de estado.
Es el equivalente, en esta arquitectura, a lo que antes hacía el ORM
directamente: "conseguir los datos", solo que ahora viajan por HTTP en
lugar de SQL.
"""

import requests
from flask import current_app

TIMEOUT = 5  # segundos máximo de espera por respuesta de la API


def obtener_productos(categoria_id=None):
    url = f"{current_app.config['API_URL']}/productos/"
    parametros = {"categoria_id": categoria_id} if categoria_id is not None else {}
    try:
        respuesta = requests.get(url, params=parametros, timeout=TIMEOUT)
        if respuesta.status_code == 200:
            return respuesta.json()
        else:
            return []
    except requests.RequestException:
        return []


def obtener_producto(sku):
    url = f"{current_app.config['API_URL']}/productos/{sku}"
    try:
        respuesta = requests.get(url, timeout=TIMEOUT)
        if respuesta.status_code == 200:
            return respuesta.json()
        else:
            return None
    except requests.RequestException:
        return None


def obtener_categorias():
    url = f"{current_app.config['API_URL']}/categorias/"
    try:
        respuesta = requests.get(url, timeout=TIMEOUT)
        if respuesta.status_code == 200:
            return respuesta.json()
        else:
            return []
    except requests.RequestException:
        return []