from flask_restful import Resource
from flask import request, jsonify
from main.models import VehicleModel
from .. import db
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from main.auth.decorators import admin_required



class Vehicle(Resource):
    @jwt_required(optional=True)
    def get(self, id):
        vehicle = db.session.query(VehicleModel).get_or_404(id)
        return vehicle.to_json()
    
    @jwt_required()
    def delete(self, id):
        vehicle = db.session.query(VehicleModel).get_or_404(id)
        db.session.delete(vehicle)
        db.session.commit()
        return '', 204
    
    @jwt_required()
    def put(self, id):
        vehicle = db.session.query(VehicleModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(vehicle, key, value)
        db.session.add(vehicle)
        db.session.commit()
        return vehicle.to_json(), 201

    
class Vehicles(Resource):
    @admin_required
    def get(self):
        vehicles = db.session.query(VehicleModel).all()
        return jsonify([vehicle.to_json() for vehicle in vehicles])
    @admin_required
    def post(self):
        vehicle = VehicleModel.from_json(request.get_json())
        db.session.add(vehicle)
        db.session.commit()
        return vehicle.to_json(), 201