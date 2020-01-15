from flask import Blueprint
from flask_restful import Api

from api.root.resource import HealthcheckView

healthcheck = Blueprint('healthcheck_bp', __name__)
api_hc = Api(healthcheck)
api_hc.add_resource(HealthcheckView, '/healthcheck')
