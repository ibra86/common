from flask import Blueprint
from flask_restful import Api

from routes.stuff.resource import StuffView

stuff = Blueprint('stuff', __name__)
api = Api(stuff)

api.add_resource(StuffView, '/stuff', '/stuff/<string:passport_id>')
