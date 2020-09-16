import json
import random

import requests
from django.http import HttpResponse, Http404

POCKEMON_URL = 'https://pokeapi.co/api/v2/pokemon'

SIMPLE_TEMPLATE = """
<html>
<head>
    <title>Pokemon</title>
</head>
<body>
    <a href="/pokemon">GIVE ME POKEMONS</a>
</body>
</html>
"""


def health_check(request):
    return HttpResponse("OK")


def index(request):
    return HttpResponse(SIMPLE_TEMPLATE)


def pokemon(request):
    random_offset = random.randint(0, 963)  # get random offset parameter required by pokemon api
    response = requests.get(POCKEMON_URL, params={'offset': random_offset, 'limit': 1})
    response = response.json()
    response = response.get('results')
    try:
        response = response[0]
        return HttpResponse(json.dumps(response), content_type="application/json")
    except:
        raise Http404('Error is happened trying to get a pokemon')
