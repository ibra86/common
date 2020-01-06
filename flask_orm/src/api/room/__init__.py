from flask import Blueprint
from flask_restful import Api

from api.room.resource import RoomView

room = Blueprint('room_bp', __name__)
api = Api(room)

api.add_resource(RoomView, '/room', '/room/<int:number>')
