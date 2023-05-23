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
    
    '''def put(self, id):
        parking = ParkingModel.query.get_or_404(id)
        data = request.get_json()

        date_of_admission_str = data.get('date_of_admission')
        date_of_admission = datetime.strptime(date_of_admission_str, '%Y-%m-%d %H:%M:%S')
        date_of_exit_str = data.get('date_of_exit')
        date_of_exit = datetime.strptime(date_of_exit_str, '%Y-%m-%d %H:%M:%S')

        parking.date_of_admission = date_of_admission
        parking.date_of_exit = date_of_exit
        parking.vehicle_patent = data.get('vehicle_patent')
        db.session.commit()

        return parking.to_json(), 201

    '''
    def put(self, id):
        parking = ParkingModel.query.get_or_404(id)
        data = request.get_json()

        date_of_admission_str = data.get('date_of_admission')
        date_of_admission = datetime.strptime(date_of_admission_str, '%Y-%m-%d %H:%M:%S')
        date_of_exit_str = data.get('date_of_exit')
        date_of_exit = datetime.strptime(date_of_exit_str, '%Y-%m-%d %H:%M:%S')

        parking.date_of_admission = date_of_admission
        parking.date_of_exit = date_of_exit
        parking.vehicle_patent = data.get('vehicle_patent')
        db.session.commit()

        # Create a record
        record = RecordModel(
            date_of_admission=date_of_admission,
            date_of_exit=date_of_exit,
            vehicle_patent=parking.vehicle_patent,
            parking_id=parking.id
        )
        db.session.add(record)
        db.session.commit()

        return parking.to_json(), 201

class Parkings(Resource):
    def get(self):
        parkings = db.session.query(ParkingModel).all()
        return jsonify([parking.to_json() for parking in parkings])
            
    def post(self):

        max_parking = db.session.query(ParkingModel).count()
        if max_parking >= 3:
            return 'No hay estacionamientos disponibles', 400
        data = request.get_json()
        parking = ParkingModel.from_json(data)  
        db.session.add(parking)
        db.session.commit()
        return parking.to_json(), 201
