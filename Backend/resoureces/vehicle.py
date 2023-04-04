from flask_restful import Resource
from flask import request, jsonify
from .. import db



class Vehicle(Resource):
    def get(self, id):
        vehicle = db.session.query(Vehicle).get_or_404(id)
        return vehicle.to_json()
    
    def put(self, id):
        vehicle = db.session.query(Vehicle).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(vehicle, key, value)
        db.session.add(vehicle)
        db.session.commit()
        return vehicle.to_json(), 201
    
    def delete(self, id):
        vehicle = db.session.query(Vehicle).get_or_404(id)
        db.session.delete(vehicle)
        db.session.commit()
        return '', 204
    
class Vehicles(Resource):
    def get(self):
        vehicles = db.session.query(Vehicle).all()
        return jsonify([vehicle.to_json() for vehicle in vehicles])
    
    def post(self):
        data = request.get_json()
        vehicle = Vehicle(**data)
        db.session.add(vehicle)
        db.session.commit()
        return vehicle.to_json(), 201