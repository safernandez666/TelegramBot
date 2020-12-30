import requests, json, iocextract
from trend import send_ioc

""" Chiste de Prueba """
def get_chiste():

    joke=requests.get('https://api.chucknorris.io/jokes/random')
    data=joke.json()

    return data["value"]

""" Parseo del Contenido IP's | Hash """
def get_ips(content):
    array_ips = []
    for ips in iocextract.extract_ips(content):
        array_ips.append(ips)
    return array_ips

def get_hash(content):
    array_hashes = []
    for hashes in iocextract.extract_hashes(content):
        array_hashes.append(hashes)
    return array_hashes