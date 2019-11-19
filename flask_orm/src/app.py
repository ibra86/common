from flask import Flask
# from werkzeug.exceptions import HTTPException
#
# from config import run_config
# from routes.room import room
# from routes.stuff import stuff
# from routes.tenant import tenant
from flask_sqlalchemy import SQLAlchemy

from config import run_config
from db import db
from routes.error.template import page_not_found
from routes.room import room
from routes.room.stubs.db_init import db_init_room
from routes.root import healthcheck
from model import RoomModel


def create_app():
    app = Flask(__name__)
    app.config.from_object(run_config())
    db.init_app(app)
    # for _t in db.tables:
    #     print("Table: %s" % _t)
    # db.session.commit()

    with app.app_context():
        # db.create_all()
        # db.session = db_init_room(db)
        # db.session.commit()

        # @app.before_first_request
        # def create_tables():
        #     db.create_all()

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
