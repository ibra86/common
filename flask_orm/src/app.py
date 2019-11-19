from flask import Flask
# from werkzeug.exceptions import HTTPException
#
# from config import run_config
# from routes.room import room
# from routes.stuff import stuff
# from routes.tenant import tenant
from flask_sqlalchemy import SQLAlchemy

from config import run_config
from routes.error.template import page_not_found
from routes.root import healthcheck


def create_app():
    app = Flask(__name__)
    app.config.from_object(run_config())
    db = SQLAlchemy(app)

    with app.app_context():
        app.register_blueprint(healthcheck)

        app.register_error_handler(404, page_not_found)

    #     app.register_blueprint(room)
    #     app.register_blueprint(tenant)
    #     app.register_blueprint(stuff)
    #     app.config.from_object(run_config())
    #
    #     @app.errorhandler(404)
    #     def page_not_found(e):
    #         code = 404
    #         if isinstance(e, HTTPException):
    #             code = e.code
    #         return jsonify(error=str(e)), code
    #
    return app
