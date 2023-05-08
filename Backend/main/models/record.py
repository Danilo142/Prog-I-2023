'''
from .. import db

class Parking(db.Model):
    __tablename__ = 'parking'
    id = db.Column(db.Integer, primary_key=True)
    date_of_admission = db.Column(db.DateTime, nullable=False)
    date_of_exit = db.Column(db.DateTime, nullable=False)
    
    #Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    patents = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)

'''