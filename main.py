from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, request
import requests

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('pages', type=str)

class HelloWorld(Resource):
    def get(self):
        pages = request.args.get('pages')
        r = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page='+str(pages)+'&sparkline=fals')
        return r.json();

api.add_resource(HelloWorld, '/api/coingecko')

if __name__ == '__main__':
    app.run(debug=True)