from flask import request
from flask_restful import Resource, fields, marshal_with, marshal
from flask_restful import reqparse

# from db import DB
# from model import Room
#
# room_resource_fields = {'id': fields.Integer,
#                         'number': fields.Integer,
#                         'level': fields.Integer,
#                         'status': fields.String,
#                         'price': fields.Float}


#
from model import RoomModel
from routes.room.marshal_structure import fields_structure

parser = reqparse.RequestParser()
parser.add_argument('filter', type=str, default='all',
                    choices=('availableOnly', 'closedOnly', 'all'),
                    help='Filter by status: "availableOnly", "closedOnly" or "all"')


class RoomView(Resource):
    @marshal_with(fields_structure)
    def get(self, number=None):
        args = parser.parse_args()

        if number:
            data = RoomModel.query.get()
            # return [x for x in DB['room'] if x.number == number]
        # else:
        #     if args['filter'] == 'availableOnly':
        #         return [r for r in DB['room'] if r.status == 'available']
        #     elif args['filter'] == 'closedOnly':
        #         return [r for r in DB['room'] if r.status == 'closed']
        #     else:
        #         return DB['room']
#
#     def post(self):
#         data = request.get_json()
#
#         # pre-validation
#         data = marshal(data, room_resource_fields)
#
#         if data not in marshal(DB['room'], room_resource_fields) and any(list(data.values())):
#             data = dict(data)
#             data = Room(**data)
#             DB['room'].append(data)
#             return "object is added", 200
#         return "object is empty or already in DB", 200
#
#     def patch(self, number=None):
#         data = request.get_json()
#         if number:
#             room_patch = [x for x in DB['room'] if x.number == number][0]
#             data = {k: data[k] for k in room_patch.__dict__ if k in data}  # only available keys
#             if {k: v for k, v in data.items() if room_patch.__dict__[k] != v}:  # if needs to be updated
#                 room_patch.__dict__.update(data)
#                 DB['room'] = [x if x.number != number else room_patch for x in DB['room']]
#                 return "object is patched", 200
#         return "no object has been patched", 200
#
#     def delete(self, number):
#
#         if number:
#
#             if number in [x.number for x in DB['room']]:
#                 DB['room'] = [x for x in DB['room'] if x.number != number]
#                 return "object is deleted", 200
#         return "no object has been deleted", 200
