from flask import request
from flask_restful import Resource, fields, marshal_with, marshal, reqparse

from api.tenant.marshal_structure import fields_structure
from db import db
from model import TenantModel


Model = TenantModel

class TenantView(Resource):

    @marshal_with(fields_structure)
    def get(self, passport_id=None):

        if passport_id:
            return Model.query.filter_by(passport_id=passport_id).all()
        else:
            return Model.query.all()

    # def post(self):
    #     data = request.get_json()
    #     data = marshal(data, fields_structure)
    #
    #     if data not in marshal(DB['tenant'], fields_structure) and any(list(data.values())):
    #         data = dict(data)
    #         data = Tenant(**data)
    #         DB['tenant'].append(data)
    #         return "object is added", 200
    #     return "object is empty or already in DB", 200
    #
    # def patch(self, passport_id=None):
    #     data = request.get_json()
    #     if passport_id:
    #         tenant_patch = [x for x in DB['tenant'] if x.passport_id == passport_id][0]
    #         data = {k: data[k] for k in tenant_patch.__dict__ if k in data}  # only available keys
    #         if {k: v for k, v in data.items() if tenant_patch.__dict__[k] != v}:  # if needs to be updated
    #             tenant_patch.__dict__.update(data)
    #             DB['tenant'] = [x if x.passport_id != passport_id else tenant_patch for x in DB['tenant']]
    #             return "object is patched", 200
    #     return "no object has been patched", 200
    #
    # def delete(self, passport_id):
    #
    #     if passport_id:
    #
    #         if passport_id in [x.passport_id for x in DB['tenant']]:
    #             DB['tenant'] = [x for x in DB['tenant'] if x.passport_id != passport_id]
    #             return "object is deleted", 200
    #     return "no object has been deleted", 200
