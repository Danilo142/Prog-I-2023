from flask_restful import Resource
from flask import request, jsonify
from main.models import VehicleModel
from .. import db



class Vehicle(Resource):
    
    def get(self, id):
        vehicle = db.session.query(VehicleModel).get_or_404(id)
        return vehicle.to_json()
    
    def delete(self, id):
        vehicle = db.session.query(VehicleModel).get_or_404(id)
        db.session.delete(vehicle)
        db.session.commit()
        return '', 204
    
    def put(self, id):
        vehicle = db.session.query(VehicleModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(vehicle, key, value)
        db.session.add(vehicle)
        db.session.commit()
        return vehicle.to_json(), 201




    '''def get(self, id):
        vehicle = db.session.query(VehicleModel).get_or_404(id)
        return vehicle.to_json()
    
    def delete(self, id):
        vehicle = db.session.query(VehicleModel).get_or_404(id)
        db.session.delete(vehicle)
        db.session.commit()
        return '', 204
    
    def put(self, id):
        vehicle = db.session.query(VehicleModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(vehicle, key, value)
        db.session.add(vehicle)
        db.session.commit()
        return vehicle.to_json(), 201'''
    
class Vehicles(Resource):
    def get(self):
        vehicles = db.session.query(VehicleModel).all()
        return jsonify([vehicle.to_json() for vehicle in vehicles])
    
    def post(self):
        vehicle = VehicleModel.from_json(request.get_json())
        db.session.add(vehicle)
        db.session.commit()
        return vehicle.to_json(), 201