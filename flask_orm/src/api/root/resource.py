from flask_restful import Resource

from sqlalchemy import create_engine

from config import Config


class HealthcheckView(Resource):

    def get(self):
        try:
            engine_url = Config.SQLALCHEMY_DATABASE_URI
            engine = create_engine(engine_url)
            connection = engine.connect()
            connection.close()
        except:
            return {"message": "DB connection issue"}, 502
        return {"message": "OK"}, 200
