from flask import Flask, make_response
from flask_restful import Resource, Api
from flask_cors import CORS
import json

from products import ProductDAO

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

class Products(Resource):
    def __init__(self) -> None:
        self.dao = ProductDAO()

    def get(self):
        all = json.dumps(self.dao.all(), ensure_ascii=False)
        response = make_response(all)
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response

class Configuration(Resource):
    def get(self):
        return {
            'phoneNumber': '5492323364927',
            'phoneNumberHumanFriendly': '2323 364927',
            'magazineLink': 'https://viewer.ipaper.io/natura-cosmeticos-sa/ar/2021/16/es-ar/revista/ciclo-16/'
        }

api.add_resource(Products, '/api/products')
api.add_resource(Configuration, '/api/config')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
