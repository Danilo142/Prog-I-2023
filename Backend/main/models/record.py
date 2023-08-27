from .. import db
from datetime import datetime

class Record(db.Model):
    __tablename__ = 'record'
    id = db.Column(db.Integer, primary_key=True)
    source_space_id = db.Column(db.Integer, db.ForeignKey('parking.id'), nullable=False)
    destination_space_id = db.Column(db.Integer, db.ForeignKey('parking.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

  

    def __repr__(self):
        return f'<Record {self.id}>, {self.source_space_id}, {self.destination_space_id}, {self.timestamp}'

    def to_json(self):
            return {
                'id': self.id,
                'source_space_id': self.source_space_id,
                'destination_space_id': self.destination_space_id,
                'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            }