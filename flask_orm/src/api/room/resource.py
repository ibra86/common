from flask import request
from flask_restful import Resource, marshal_with
from flask_restful import reqparse

from api.room.marshal_structure import fields_structure
from db import db
from model import RoomModel

parser = reqparse.RequestParser()
parser.add_argument('filter', type=str, default='all',
                    choices=('availableOnly', 'closedOnly', 'all'),
                    help='Filter by status: "availableOnly", "closedOnly" or "all"')

Model = RoomModel


class RoomView(Resource):

    @marshal_with(fields_structure)
    def get(self, number=None):
        args = parser.parse_args()

        if number:
            return Model.query.filter_by(number=number).all()
        else:
            if args['filter'] == 'availableOnly':
                return Model.query.filter_by(status='available').all()
            elif args['filter'] == 'closedOnly':
                return Model.query.filter_by(status='closed').all()
            else:
                return Model.query.all()

    def post(self):
        data = request.get_json()

        if not Model.query.filter_by(number=data.get('number')).all():
            obj = Model(**data)
            db.session.add(obj)
            db.session.commit()
            return "object is added", 201
        return "object is already in DB", 200

    def patch(self, number=None):
        data = request.get_json()
        if number:
            Model.query.filter_by(number=number).update(data)
            db.session.commit()
            return "object is patched if existed", 201
        return "no object has been patched", 200

    def delete(self, number):

        if number:
            Model.query.filter_by(number=number).delete()
            db.session.commit()
            return "object is deleted if existed", 200

        return "no object has been deleted", 200
