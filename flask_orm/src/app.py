from api.root import healthcheck
from flask import Flask

from config import run_config
from db import db
from api.error.template import page_not_found
from api.room import room
from api.stubs.db_init_room import db_init_room


def create_app():
    app = Flask(__name__)
    app.config.from_object(run_config())
    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.drop_all(app=app)
        db.create_all(app=app)
        db.session = db_init_room(db)
        db.session.commit()

    app.register_blueprint(healthcheck)
    app.register_error_handler(404, page_not_found)

    app.register_blueprint(room)

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
