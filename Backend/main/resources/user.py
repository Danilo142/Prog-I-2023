from flask_restful import Resource
from flask import request, jsonify
from main.models import UserModel
from .. import db
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from main.auth.decorators import admin_required


class User(Resource):
    @jwt_required(optional=True)
    def get(self, id):
        user = db.session.query(UserModel).get_or_404(id)
        return user.to_json()
    
    @jwt_required()
    def delete(self, id):
        user = db.session.query(UserModel).get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return '', 204
    
    @jwt_required()
    def put(self, id):
        user = db.session.query(UserModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(user, key, value)
        db.session.add(user)
        db.session.commit()
        return user.to_json(), 201
    
class Users(Resource):
    @admin_required
    def get(self):
        users = db.session.query(UserModel).all()
        return jsonify([user.to_json() for user in users])
    
    @admin_required
    def post(self):
        user = UserModel.from_json(request.get_json())
        db.session.add(user)
        db.session.commit()
        return user.to_json(), 201  