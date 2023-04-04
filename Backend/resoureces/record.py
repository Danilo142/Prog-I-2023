from flask_restful import Resource
from flask import request, jsonify
from .. import db


class Record(Resource):
    def get(self, id):
        record = db.session.query(Record).get_or_404(id)
        return record.to_json()
    
    def put(self, id):
        record = db.session.query(Record).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(record, key, value)
        db.session.add(record)
        db.session.commit()
        return record.to_json(), 201
    
    def delete(self, id):
        record = db.session.query(Record).get_or_404(id)
        db.session.delete(record)
        db.session.commit()
        return '', 204
    
    def update(self, id):
        record = db.session.query(Record).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(record, key, value)
        db.session.add(record)
        db.session.commit()
        return record.to_json(), 201
    
class Records(Resource):
    def get(self):
        records = db.session.query(Records).all()
        return jsonify([record.to_json() for record in records])
    
    def post(self):
        data = request.get_json()
        records = Records(**data)
        db.session.add(records)
        db.session.commit()
        return records.to_json(), 201