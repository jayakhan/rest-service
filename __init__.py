from flask import Flask
from flask_restful import Resource, Api

app = Flask('content-extract-v1')
app = Flask(__name__.split('.')[0])
api = Api(app)
