from flask import Blueprint
from flask_restful import Api

from api.tenant.resource import TenantView

tenant = Blueprint('tenant', __name__)
api = Api(tenant)

api.add_resource(TenantView, '/tenant', '/tenant/<string:passport_id>')
