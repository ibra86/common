from flask import request
from flask_restful import Resource, fields, marshal_with, marshal

from db import DB
from model import Tenant

city_structure = {
    "city": fields.String,
    "street": fields.String
}
tenant_resource_fields = {'name': fields.String,
                          'passport_id': fields.String,
                          'age': fields.Integer,
                          'sex': fields.String,
                          'address': fields.Nested(city_structure),
                          'room_number': fields.Integer}


class TenantView(Resource):
    @marshal_with(tenant_resource_fields)
    def get(self, passport_id=None):

        if passport_id:
            return [x for x in DB['tenant'] if x.passport_id == passport_id]
        else:
            return DB['tenant']

    def post(self):
        data = request.get_json()
        data = marshal(data, tenant_resource_fields)

        if data not in marshal(DB['tenant'], tenant_resource_fields) and any(list(data.values())):
            data = dict(data)
            data = Tenant(**data)
            DB['tenant'].append(data)
            return "object is added", 200
        return "object is empty or already in DB", 200

    def patch(self, passport_id=None):
        data = request.get_json()
        if passport_id:
            tenant_patch = [x for x in DB['tenant'] if x.passport_id == passport_id][0]
            data = {k: data[k] for k in tenant_patch.__dict__ if k in data}  # only available keys
            if {k: v for k, v in data.items() if tenant_patch.__dict__[k] != v}:  # if needs to be updated
                tenant_patch.__dict__.update(data)
                DB['tenant'] = [x if x.passport_id != passport_id else tenant_patch for x in DB['tenant']]
                return "object is patched", 200
        return "no object has been patched", 200

    def delete(self, passport_id):

        if passport_id:

            if passport_id in [x.passport_id for x in DB['tenant']]:
                DB['tenant'] = [x for x in DB['tenant'] if x.passport_id != passport_id]
                return "object is deleted", 200
        return "no object has been deleted", 200
