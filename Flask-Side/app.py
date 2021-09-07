from flask import Flask
from flask_restful import Api
from flask_cors import CORS

#Resources aka logic for each route
from resources.home import Home


app = Flask(__name__)
api = Api(app)
CORS(app)


api.add_resource(Home, '/', '/home')

if __name__ == '__main__':
    app.run(port=5002, debug=True)