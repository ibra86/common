import json

from flask import Response, request
from flask_restful import Resource
from src.insrastructure import DB
from src.model import City


class CityView(Resource):
    def get(self, id_):
        data_dict = [{'name': x.name, 'id': x.id} for x in DB['city']]
        data = json.dumps(data_dict)
        return Response(data, status=200)

    def post(self, id_):
        data = request.json
        DB['city'].append(City(data['name']))
        return Response(status=200)

    def delete(self, id_):
        DB['city'] = [x for x in DB['city'] if x.id != id_]
        return Response(status=200)
