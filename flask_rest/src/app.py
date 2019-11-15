from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException

from routes.room import room


def create_app():
    app = Flask(__name__)
    # api = Api(app)

    app.register_blueprint(room)
    # app.config.from_object(run_config())

    @app.errorhandler(404)
    def page_not_found(e):
        code = 404
        if isinstance(e, HTTPException):
            code = e.code
        return jsonify(error=str(e)), code

    return app