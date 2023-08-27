from flask_restful import Resource
from flask import request, jsonify
from main.models import RecordModel, ParkingModel
from .. import db
from datetime import datetime
from sqlalchemy import inspect

class Records(Resource):
    def get(self):
        records = db.session.query(RecordModel).all()
        return jsonify([record.to_json() for record in records])

class Record(Resource):
    def get(self, id):
        record = db.session.query(RecordModel).get_or_404(id)
        return record.to_json()

