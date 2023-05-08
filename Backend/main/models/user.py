from .. import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    
    #foreign keys
    patents = db.Column(db.Integer, db.ForeignKey('vehicle.patents'), nullable=False)

    #Relaciones
    vehicle = db.relationship('Vehicle', backref='user', lazy=True)
    parking = db.relationship('Parking', backref='user', lazy=True)

    #esto es para que no se repitan los datos en la base de datos en la tabla user 
    def __repr__(self):
        return '<User %r>' % self.id, self.name, self.email, self.password
    # esto es para que se muestre en formato json
    def to_json(self):
        json_user = {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password
        }
        return json_user
    
    def from_json(json_user):
        id = json_user.get('id')
        name = json_user.get('name')
        email = json_user.get('email')
        password = json_user.get('password')
        return User(id=id, name=name, email=email, password=password)