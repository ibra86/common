from flask import Blueprint
from flask_restful import Api

from routes.room.resource import RoomView

room = Blueprint('room', __name__)
api = Api(room)

api.add_resource(RoomView, '/room', '/room/<int:number>')
