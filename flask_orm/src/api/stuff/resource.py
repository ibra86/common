from flask import request
from flask_restful import Resource, marshal_with

from api.stuff.marshal_structure import fields_structure
from db import db
from model import StuffModel

Model = StuffModel


class StuffView(Resource):
    @marshal_with(fields_structure)
    def get(self, passport_id=None):

        if passport_id:
            return Model.query.filter(passport_id=passport_id).all()
        else:
            return Model.query.all()

    def post(self):
        data = request.get_json()

        if Model.query.filter_by(passport_id=data.get('passport_id')).all():
            obj = Model(**data)
            db.session.add(obj)
            db.session.commit()
            return "object is added", 201
        return "no object has been added", 200

    def patch(self, passport_id=None):
        data = request.get_json()
        if passport_id:
            Model.query.filter_by(number=passport_id).update(data)
            db.session.commit()
            return "object is patched if existed", 201
        return "no object has been patched", 200

    def delete(self, passport_id):

        if passport_id:
            Model.query.filter_by(passport_id=passport_id).delete()
            db.session.commit()
            return "object is deleted if existed", 200
        return "no object has been deleted", 200
