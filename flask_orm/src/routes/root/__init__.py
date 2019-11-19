from flask import Blueprint
from flask_restful import Api

from routes.root.resource import HealthcheckView

healthcheck = Blueprint('healthcheck_bp', __name__)
api = Api(healthcheck)

api.add_resource(HealthcheckView, '/healthcheck')

#
