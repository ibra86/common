from flask import Flask
from flask_restful import Api

from config import run_config
from routes.room import RoomView

app = Flask(__name__)
api = Api(app)

app.config.from_object(run_config())

api.add_resource(RoomView, '/room/<int:number>')

if __name__ == '__main__':
    app.run(debug=True)