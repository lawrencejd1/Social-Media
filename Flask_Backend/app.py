from flask import Flask, Blueprint
from flask_restful import Api
from flask_cors import CORS

#Resources aka logic for each route
from resources.home import Home


app = Flask(__name__)
app_bp = Blueprint('api', __name__)
api = Api(app_bp)
CORS(app)


api.add_resource(Home, '/', '/home')

if __name__ == '__main__':
    app.register_blueprint(app_bp)
    app.run(port=5000, debug=True)
    