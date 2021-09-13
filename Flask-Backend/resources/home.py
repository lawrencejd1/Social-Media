import json

from flask_restful import Resource


class Home(Resource):
    def index(self):
        return "Hello World"

    def get(self):
        return {"data":{
                    "title":"Hello World!",
                    "body":"THis is the body of the website"}
                    }