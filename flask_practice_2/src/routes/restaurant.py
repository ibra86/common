import json

from flask import Blueprint
from flask import Response, request
from src.insrastructure import DB
from src.model import Restaurant

restaurant = Blueprint('restaurant', __name__)


@restaurant.route('/restaurants', methods=['GET'])
def all_restaurants():
    rests = [{'name': rest.name, 'stars': rest.stars, 'id': rest.id} for rest in DB['restaurant']]
    data = json.dumps(rests)
    return Response(data, status=200)


@restaurant.route('/restaurants', methods=['POST'])
def restaurants_create():
    data = request.json
    DB['restaurant'].append(Restaurant(data['name'], data['stars']))
    return Response(status=200)
