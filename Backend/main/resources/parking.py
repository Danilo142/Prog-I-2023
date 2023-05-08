from flask_restful import Resource
from flask import request, jsonify
from .. import db


class Parking(Resource):
    def get(self, id):
        parking = db.session.query(Parking).get_or_404(id)
        return parking.to_json()
    
    def put(self, id):
        parking = db.session.query(Parking).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(parking, key, value)
        db.session.add(parking)
        db.session.commit()
        return parking.to_json(), 201
    
    def delete(self, id):
        parking = db.session.query(Parking).get_or_404(id)
        db.session.delete(parking)
        db.session.commit()
        return '', 204
    
    def update(self, id):
        parking = db.session.query(Parking).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(parking, key, value)
        db.session.add(parking)
        db.session.commit()
        return parking.to_json(), 201
    
class Parkings(Resource):
    def get(self):
        parkings = db.session.query(Parking).all()
        return jsonify([parking.to_json() for parking in parkings])
    
    def post(self):
        data = request.get_json()
        parking = Parking(**data)
        db.session.add(parking)
        db.session.commit()
        return parking.to_json(), 201