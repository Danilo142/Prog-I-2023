from flask_restful import Resource
from flask import request, jsonify
from main.models import ParkingModel
from main.models import RecordModel
from .. import db
from datetime import datetime
from sqlalchemy import inspect
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from main.auth.decorators import admin_required


class Parking(Resource):

    @jwt_required(optional=True)
    def get(self, id):
        parking = db.session.query(ParkingModel).get_or_404(id)
        return parking.to_json()
    
    @jwt_required()
    def delete(self, id):
        parking = db.session.query(ParkingModel).get_or_404(id)
        db.session.delete(parking)
        db.session.commit()
        return '', 204
    
    """def put(self, id):
        parking = db.session.query(ParkingModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            if key in ['date_of_admission', 'date_of_exit']:
                value = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
            setattr(parking, key, value)
            
        if parking.available:
            parking.available = False
            parking.date_of_admission = datetime.utcnow()
            parking.date_of_exit = None
        else:
            parking.date_of_exit = datetime.utcnow()
            parking.available = True
            parking.vehicle_patent = None

        db.session.commit()
        return parking.to_json(), 200
    """
    def put(self, id):
        parking = db.session.query(ParkingModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
           if key in ['date_of_admission', 'date_of_exit']:
               value = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
           setattr(parking, key, value)

        if parking.available:
           parking.available = False
           parking.date_of_admission = datetime.utcnow()
           parking.date_of_exit = None
        else:
           parking.date_of_exit = datetime.utcnow()
           parking.available = True
           parking.vehicle_patent = None

       # Crear instancia de Record y guardarla en la base de datos
        record = RecordModel(source_space_id=parking.id, destination_space_id=2, timestamp=datetime.utcnow())
        db.session.add(record)

        db.session.commit()
        return parking.to_json(), 200

    

class Parkings(Resource):
    def get(self):
        parkings = db.session.query(ParkingModel).all()
        return jsonify([parking.to_json() for parking in parkings])
            
    def post(self):

        data = request.get_json()
        parking = ParkingModel.from_json(data)
        db.session.add(parking)
        db.session.commit()
        return parking.to_json(), 201
