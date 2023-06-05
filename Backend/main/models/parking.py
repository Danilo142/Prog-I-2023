from .. import db
from datetime import datetime

class Parking(db.Model):
    __tablename__ = 'parking'
    id = db.Column(db.Integer, primary_key=True)
    date_of_admission = db.Column(db.DateTime, nullable=True)
    date_of_exit = db.Column(db.DateTime, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=False)
    # Foreign Keys
    vehicle_patent = db.Column(db.Integer, db.ForeignKey('vehicle.patent'), nullable=True, unique=True)
    
    # Relationships
    vehicle = db.relationship('Vehicle', back_populates='parkings', lazy=True)

    records = db.relationship('Record', back_populates='parking', lazy=True)

    def __repr__(self):
        return '<Parking %r>' % self.id, self.date_of_admission, self.date_of_exit, self.available, self.vehicle_patent

    '''def to_json(self):
        json_parking = {
            'id': self.id,
            'date_of_admission': self.date_of_admission.strftime('%Y-%m-%d %H:%M:%S'),
            'date_of_exit': self.date_of_exit.strftime('%Y-%m-%d %H:%M:%S'),
            'vehicle_patent': self.vehicle_patent,
            'available': self.available
        }
        return json_parking
'''
    def to_json(self):
        json_parking = {
            'id': self.id,
            'available': self.available
        }
        if self.date_of_admission is not None:
            json_parking['date_of_admission'] = self.date_of_admission.strftime('%Y-%m-%d %H:%M:%S')
        if self.date_of_exit is not None:
            json_parking['date_of_exit'] = self.date_of_exit.strftime('%Y-%m-%d %H:%M:%S')
        if self.vehicle_patent is not None:
            json_parking['vehicle_patent'] = self.vehicle_patent
        return json_parking


    def from_json(json_parking):
        id = json_parking.get('id')
        date_of_admission_str = json_parking.get('date_of_admission')
        date_of_exit_str = json_parking.get('date_of_exit')
        vehicle_patent = json_parking.get('vehicle_patent')
        available = json_parking.get('available')

        date_of_admission = datetime.strptime(date_of_admission_str, '%Y-%m-%d %H:%M:%S') if date_of_admission_str else None
        date_of_exit = datetime.strptime(date_of_exit_str, '%Y-%m-%d %H:%M:%S') if date_of_exit_str else None
        return Parking(id=id, date_of_admission=date_of_admission, date_of_exit=date_of_exit, vehicle_patent=vehicle_patent, available=available)