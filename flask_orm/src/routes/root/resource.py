from flask_restful import Resource


class HealthcheckView(Resource):

    def get(self):
        return {"message": "OK"}, 200
