import json

import requests

IPINFO_URL = 'http://ipinfo.io/{ip}/json'


def get_ip_country(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""
    r=requests.get(IPINFO_URL[0:16],ip_address)
    data=r.text
    jsondata=json.loads(data)
    return jsondata['country']