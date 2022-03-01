from django.http.response import Http404, HttpResponse
from msilib.schema import ListView
from django.shortcuts import render
import requests

# Create your views here.

def publicar(request):
    token = refreshToken()
    jsonPublicar = {
            "title":"Item de test - No Ofertar",
            "category_id":"MLV436797",
            "price":2302,
            "currency_id":"USD",
            "available_quantity":10,
            "buying_mode":"buy_it_now",
            "condition":"new",
            "listing_type_id":"gold_special",
            "sale_terms":[
                {
                    "id":"WARRANTY_TYPE",
                    "value_name":"Garantía del vendedor"
                },
                {
                    "id":"WARRANTY_TIME",
                    "value_name":"90 días"
                }
            ],
            "pictures":[
                {
                    "source":"http://mla-s2-p.mlstatic.com/968521-MLA20805195516_072016-O.jpg"
                }
            ],
            "attributes":[
                {
                    "id":"BRAND",
                    "value_name":"Marca del producto"
                },
                {
                    "id":"EAN",
                    "value_name":"7898095297749"
                }
            ]
            }
    response = requests.post(
        'https://api.mercadolibre.com/items',
        headers={'Authorization': 'Bearer ' + token},
        json=jsonPublicar
    )
    print(response.json())
    return HttpResponse(token)


def refreshToken():
    response = requests.post(
            'https://api.mercadolibre.com/oauth/token', 
            headers={'Accept': 'application/json', 
                'Content-Type': 'application/x-www-form-urlencoded'},
            data={'grant_type': 'refresh_token', 
                'client_id': '2223042557909195', 
                'client_secret': 'ccG704MccTgKJWbtxpBKCByXylX9W2yi', 
                'refresh_token': 'TG-621d4504d3c829001a9cddd9-1081981455'})

    a = response.json()
    token = a["access_token"]
    return token