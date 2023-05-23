from .. import db
from datetime import datetime

class Record(db.Model):
    __tablename__ = 'record'
    id = db.Column(db.Integer, primary_key=True)

    # Parking fields
    date_of_admission = db.Column(db.DateTime, nullable=False)
    date_of_exit = db.Column(db.DateTime, nullable=False)
    vehicle_patent = db.Column(db.Integer, nullable=False)

    # Foreign Keys
    parking_id = db.Column(db.Integer, db.ForeignKey('parking.id'), nullable=False)

    # Relationships
    parking = db.relationship('Parking', back_populates='records', lazy=True)

    def __repr__(self):
        return '<Record %r>' % self.id

    def to_json(self):
        json_record = {
            'id': self.id,
            'parking_id': self.parking_id,
            'date_of_admission': self.date_of_admission.strftime('%Y-%m-%d %H:%M:%S'),
            'date_of_exit': self.date_of_exit.strftime('%Y-%m-%d %H:%M:%S'),
            'vehicle_patent': self.vehicle_patent
        }
        return json_record

    @staticmethod
    def from_json(json_record):
        id = json_record.get('id')
        parking_id = json_record.get('parking_id')
        date_of_admission_str = json_record.get('date_of_admission')
        date_of_exit_str = json_record.get('date_of_exit')
        vehicle_patent = json_record.get('vehicle_patent')

        date_of_admission = datetime.strptime(date_of_admission_str, '%Y-%m-%d %H:%M:%S')
        date_of_exit = datetime.strptime(date_of_exit_str, '%Y-%m-%d %H:%M:%S')
        return Record(
            id=id,
            parking_id=parking_id,
            date_of_admission=date_of_admission,
            date_of_exit=date_of_exit,
            vehicle_patent=vehicle_patent
        )
