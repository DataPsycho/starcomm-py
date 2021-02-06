from flask_restful import Resource, Api, marshal, marshal_with
from flask import Flask, request
from .service import reply
from .model import request_fields, response_fields


class Discovery(Resource):
    @marshal_with(response_fields)
    def post(self):
        req = marshal(request.get_json(), request_fields)
        return reply(req)


def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Discovery, '/discovery')
    return app
