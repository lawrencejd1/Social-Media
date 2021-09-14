from flask import jsonify

from flask_restful import Resource


class Home(Resource):
    def get(self):
      
        data = {"title":"Hello World!", "body":"THis is the body of the website"}
        
        return jsonify(data)