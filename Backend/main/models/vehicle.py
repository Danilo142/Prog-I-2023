from .. import db   

class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    patent = db.Column(db.Integer, primary_key=True, autoincrement=False)
    model = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(50), nullable=False)

    #Foreign Keys
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    #Relaciones
    owner = db.relationship('User', back_populates='vehicles', lazy=True)
    parkings = db.relationship('Parking', back_populates='vehicle', lazy=True)
    
    def __repr__(self):
        return '<Vehicle %r>' % self.patent, self.model, self.color, self.owner_id

    def to_json(self):
        json_vehicle = {
            'patent': self.patent,
            'model': self.model,
            'color': self.color,
            'user_id': self.owner_id
        }
        return json_vehicle
    
    def from_json(json_vehicle):
        patent = json_vehicle.get('patent')
        model = json_vehicle.get('model')
        color = json_vehicle.get('color')
        user_id = json_vehicle.get('user_id')
        return Vehicle(patent=patent, model=model, color=color, owner_id=user_id)
    