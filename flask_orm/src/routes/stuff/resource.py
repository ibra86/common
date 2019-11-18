from flask import request
from flask_restful import Resource, fields, marshal_with, marshal

from db import DB
from model import Stuff

stuff_resource_fields = {'name': fields.String,
                         'passport_id': fields.String,
                         'position': fields.String,
                         'salary': fields.Integer}


class StuffView(Resource):
    @marshal_with(stuff_resource_fields)
    def get(self, passport_id=None):

        if passport_id:
            return [x for x in DB['stuff'] if x.passport_id == passport_id]
        else:
            return DB['stuff']

    def post(self):
        data = request.get_json()
        data = marshal(data, stuff_resource_fields)

        if data not in marshal(DB['stuff'], stuff_resource_fields) and any(list(data.values())):
            data = dict(data)
            data = Stuff(**data)
            DB['stuff'].append(data)
            return "object is added", 200
        return "object is empty or already in DB", 200

    def patch(self, passport_id=None):
        data = request.get_json()
        if passport_id:
            stuff_patch = [x for x in DB['stuff'] if x.passport_id == passport_id][0]
            data = {k: data[k] for k in stuff_patch.__dict__ if k in data}  # only available keys
            if {k: v for k, v in data.items() if stuff_patch.__dict__[k] != v}:  # if needs to be updated
                stuff_patch.__dict__.update(data)
                DB['stuff'] = [x if x.passport_id != passport_id else stuff_patch for x in DB['stuff']]
                return "object is patched", 200
        return "no object has been patched", 200

    def delete(self, passport_id):

        if passport_id:

            if passport_id in [x.passport_id for x in DB['stuff']]:
                DB['stuff'] = [x for x in DB['stuff'] if x.passport_id != passport_id]
                return "object is deleted", 200
        return "no object has been deleted", 200
