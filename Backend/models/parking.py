from .. import db

class Parking(db.Model):
    __tablename__ = 'parking'
    id = db.Column(db.Integer, primary_key=True)
    date_of_admission = db.Column(db.DateTime, nullable=False)
    date_of_exit = db.Column(db.DateTime, nullable=False)
    
    #Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)


    
    #esto es para que no se repitan los datos en la base de datos en la tabla parking 
    def __repr__(self):
        return '<Parking %r>' % self.id, self.date_of_admission, self.date_of_exit, self.user_id, self.vehicle_id
    # esto es para que se muestre en formato json
    def to_json(self):
        json_parking = {
            'id': self.id,
            'date_of_admission': self.date_of_admission,
            'date_of_exit': self.date_of_exit,
            'user_id': self.user_id,
            'vehicle_id': self.vehicle_id
        }
        return json_parking
    
    def from_json(json_parking):
        id = json_parking.get('id')
        date_of_admission = json_parking.get('date_of_admission')
        date_of_exit = json_parking.get('date_of_exit')
        user_id = json_parking.get('user_id')
        vehicle_id = json_parking.get('vehicle_id')
        return Parking(id=id, date_of_admission=date_of_admission, date_of_exit=date_of_exit, user_id=user_id, vehicle_id=vehicle_id)
    
    
       
