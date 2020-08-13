from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create engine('sqlite:///exemplo.db')
app = Flask(_name_)
api = Api(app)
