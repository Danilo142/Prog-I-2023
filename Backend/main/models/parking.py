from .. import db


from sqlalchemy import CheckConstraint



class Parking(db.Model):
    __tablename__ = 'parking'
    id = db.Column(db.Integer, primary_key=True)
    date_of_admission = db.Column(db.DateTime, nullable=False)
    date_of_exit = db.Column(db.DateTime, nullable=False)
    
    #Foreign Keys
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)

    #Relaciones
    #user = db.relationship('User', backref='parking', lazy=True)
    #vehicle = db.relationship('Vehicle', backref='parking', lazy=True)

    # Definimos la restricción CHECK para limitar la cantidad de filas
    '''__table_args__ = (
        CheckConstraint('SELECT COUNT(*) < 50 FROM mytable'),
    )
    '''                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            



    #esto es para que no se repitan los datos en la base de datos en la tabla parking 
    def __repr__(self):
        return '<Parking %r>' % self.id, self.date_of_admission, self.date_of_exit, self.user_id, self.patents
    # esto es para que se muestre en formato json
    def to_json(self):
        json_parking = {
            'id': self.id,
            'date_of_admission': self.date_of_admission,
            'date_of_exit': self.date_of_exit,
            'user_id': self.user_id,
            'patents': self.patents
        }
        return json_parking
    
    def from_json(json_parking):
        id = json_parking.get('id')
        date_of_admission = json_parking.get('date_of_admission')
        date_of_exit = json_parking.get('date_of_exit')
        user_id = json_parking.get('user_id')
        patents = json_parking.get('patents')
        return Parking(id=id, date_of_admission=date_of_admission, date_of_exit=date_of_exit, user_id=user_id, patents=patents)

    
       
