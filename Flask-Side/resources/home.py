from flask_restful import Resource
class Home(Resource):
    def get():
        return print('hello world')