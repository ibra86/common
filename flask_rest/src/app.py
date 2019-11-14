from flask import Flask

# from routes.room import RoomView
from routes.room import room


def create_app():
    app = Flask(__name__)
    # api = Api(app)

    app.register_blueprint(room)
    # app.config.from_object(run_config())

    # api.add_resource(RoomView, '/room/<int:number>')

    return app
