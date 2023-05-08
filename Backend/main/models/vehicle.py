from .. import db   

class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    patents = db.Column(db.Integer, primary_key=True, autoincrement=False, unique=True)
    model = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(50), nullable=False)

    #Foreign Keys
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    #Relaciones
    user = db.relationship('User', backref='vehicle', lazy=True)
    parking = db.relationship('Parking', backref='vehicle', lazy=True)
    
    def __repr__(self):
        return '<Vehicle %r>' % self.patents, self.model, self.color, self.owner_id

    def to_json(self):
        json_vehicle = {
            'patents': self.patents,
            'model': self.model,
            'color': self.color,
            'owner_id': self.owner_id
        }
        return json_vehicle
    
    def from_json(json_vehicle):
        patents = json_vehicle.get('patents')
        model = json_vehicle.get('model')
        color = json_vehicle.get('color')
        owner_id = json_vehicle.get('owner_id')
        return Vehicle(patents=patents, model=model, color=color, owner_id=owner_id)
    