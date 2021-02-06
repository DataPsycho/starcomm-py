from flask_restful import fields, marshal
from datetime import datetime


response_fields = {
    'to': fields.String,
    'message': fields.String,
    'respondtime': fields.String
}

request_fields = {
    'from': fields.String,
    'message': fields.String,
    'requesttime': fields.String
}


class ResponseDao:
    def __init__(self, to: str, message: str):
        self.to = to
        self.message = message
        self.respondtime = str(datetime.now())
