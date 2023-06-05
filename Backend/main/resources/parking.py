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
        if parking.available:
            data = request.get_json()
            parking.date_of_admission = datetime.strptime(data['date_of_admission'], '%Y-%m-%d %H:%M:%S')
            parking.date_of_exit = datetime.strptime(data['date_of_exit'], '%Y-%m-%d %H:%M:%S')
            parking.vehicle_patent = data['vehicle_patent']
            db.session.commit()
        else:
            record = RecordModel(
                date_of_admission=parking.date_of_admission,
                date_of_exit=parking.date_of_exit,
                vehicle_patent=parking.vehicle_patent,
                parking=parking
            )
            db.session.add(record)
            db.session.commit()

            parking.date_of_admission = None
            parking.date_of_exit = None
            parking.vehicle_patent = None   
            parking.available = True
            db.session.commit()
            
        return parking.to_json(), 200
        '''

    def put(self, id):
        parking = ParkingModel.query.get_or_404(id)
        if parking.available:
            data = request.get_json()
            try:
                parking.date_of_admission = datetime.strptime(data['date_of_admission'], '%Y-%m-%d %H:%M:%S')
            except TypeError:
                parking.date_of_admission = None
            try:
                parking.date_of_exit = datetime.strptime(data['date_of_exit'], '%Y-%m-%d %H:%M:%S')
            except TypeError:
                parking.date_of_exit = None
            parking.vehicle_patent = data['vehicle_patent'] if data['vehicle_patent'] is not None else None
            db.session.commit()
        else:
            record = RecordModel(
                date_of_admission=parking.date_of_admission,
                date_of_exit=parking.date_of_exit,
                vehicle_patent=parking.vehicle_patent,
                parking=parking
            )
            db.session.add(record)
            db.session.commit()

            parking.date_of_admission = None
            parking.date_of_exit = None
            parking.vehicle_patent = None   
            parking.available = True
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
