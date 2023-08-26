from .. import db
from datetime import datetime
from sqlalchemy.sql import func

class Parking(db.Model):
    __tablename__ = 'parking'
    id = db.Column(db.Integer, primary_key=True)
    date_of_admission = db.Column(db.DateTime, server_default = func.now(), onupdate=func.now(), nullable=True)
    date_of_exit = db.Column(db.DateTime, server_default = func.now(), onupdate=func.now(), nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=False)
    
    # Foreign Keys
    vehicle_patent = db.Column(db.Integer, db.ForeignKey('vehicle.patent'), nullable=True, unique=True)
    
    # Relationships
    vehicle = db.relationship('Vehicle', back_populates='parkings', lazy=True)


    def __repr__(self):
        return f'<Parking {self.id}>, {self.date_of_admission}, {self.date_of_exit}, {self.available}, {self.vehicle_patent}'
    
    def to_json(self):
        parking_json = {
            'id': self.id,
            'date_of_admission': self.date_of_admission.strftime('%Y-%m-%d %H:%M:%S') if self.date_of_admission else None,
            'date_of_exit': self.date_of_exit.strftime('%Y-%m-%d %H:%M:%S') if self.date_of_exit else None,
            'available': self.available,
            'vehicle_patent': self.vehicle_patent
        }
        return parking_json

    
    def from_json(self, parking_json):
        self.id = parking_json.get('id')
        self.date_of_admission = parking_json.get('date_of_admission')
        self.date_of_exit = parking_json.get('date_of_exit')
        self.available = parking_json.get('available')
        self.vehicle_patent = parking_json.get('vehicle_patent')
        return self