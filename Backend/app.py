from main.models import ParkingModel    
from main import create_app
import os
app = create_app()
app.app_context().push()
from main import db


def create_parking_spaces(num_spaces):
    for i in range(num_spaces):
        parking = ParkingModel(available=True)
        db.session.add(parking)
    db.session.commit()

if __name__ == '__main__':
    db.create_all()
    if not ParkingModel.query.first():
        create_parking_spaces(5) 
    app.run(debug = True, port = os.getenv("PORT"))

