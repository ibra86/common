from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException

from config import run_config
from routes.room import room
from routes.stuff import stuff
from routes.tenant import tenant


def create_app():
    app = Flask(__name__)

    app.register_blueprint(room)
    app.register_blueprint(tenant)
    app.register_blueprint(stuff)
    app.config.from_object(run_config())

    @app.errorhandler(404)
    def page_not_found(e):
        code = 404
        if isinstance(e, HTTPException):
            code = e.code
        return jsonify(error=str(e)), code

    return app
