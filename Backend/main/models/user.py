from .. import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    
    #Relaciones
    vehicles = db.relationship('Vehicle', back_populates='owner', cascade="all, delete-orphan", lazy=True)
    

    #Getter de la contraseña plana no permite leerla
    @property
    def plain_password(self):
        raise AttributeError('Password cannot be read')
    
    #Setter de la contraseña plana
    @plain_password.setter
    def plain_password(self, password):
        self.password = generate_password_hash(password)

    #Valida la contraseña plana con la encriptada
    def validate_pass(self, password):
        return check_password_hash(self.password, password)
    

    def __repr__(self):
        return f'< Name:{self.name}, Email:{self.email},Role:{self.role} >'



    def to_json(self):
        json_user = {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'role': self.role,
            "vehicles": [vehicle.to_json() for vehicle in self.vehicles]
        }
        return json_user
    
    def from_json(json_user):
        id = json_user.get('id')
        name = json_user.get('name')
        email = json_user.get('email')
        role = json_user.get('role')
        password = json_user.get('password')
        
        user = User(id=id, name=name, email=email, role=role)
        user.plain_password = password  # Utiliza el setter para encriptar la contraseña
        return user
