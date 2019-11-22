from flask_restful import Resource, request, marshal_with

from api.school.structures import fields_structure
from db import School as Model
from db import db

class SchoolResource(Resource):

    method_decorators = [marshal_with(fields_structure)]

    def get(self):
        return "Ok"

    def post(self):
        data = request.json
        obj = Model(**data)
        db.session.add(obj)
        db.session.commit()

        return Model.query.all(), 201