from flask import request
from flask_restful import Resource, fields, marshal_with

from db import DB
from routes.room.schema import validate_room

room_resource_fields = {'number': fields.Integer,
                        'level': fields.Integer,
                        'status': fields.String,
                        'price': fields.Float}

from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('filter', type=str, default='all',
                    choices=('availableOnly', 'closedOnly', 'all'),
                    help='Filter by status: "availableOnly", "closedOnly" or "all"')


class RoomView(Resource):
    @marshal_with(room_resource_fields)
    def get(self, number=None):
        args = parser.parse_args()

        if number:
            return [r for r in DB['room'] if r.number == number]
        else:
            if args['filter'] == 'availableOnly':
                return [r for r in DB['room'] if r.status == 'available']
            elif args['filter'] == 'closedOnly':
                return [r for r in DB['room'] if r.status == 'closed']
            else:
                return DB['room']

    def post(self):
        # data = request.get_json()
        # DB['room'].append(Room(data))
        # return Response(status=200)
        inputs = validate_room(request)
        return inputs

    def delete(self, number):
        pass
