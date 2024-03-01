from models import Pet, db
from app import app

#Create all tables
db.drop_all()
db.create_all()

#Clear table if tables aren't already empty
Pet.query.delete()

#Create a few test pets
poncho = Pet(name="Poncho Perrera", species="cat", photo_url="https://res.cloudinary.com/teepublic/image/private/s--JU9wyq1v--/c_fit,g_north_west,h_920,w_667/co_ffffff,e_outline:41/co_ffffff,e_outline:inner_fill:1/co_bbbbbb,e_outline:3:1000/c_mpad,g_center,h_1260,w_1260/b_rgb:eeeeee/c_limit,f_auto,h_630,q_auto:good:420,w_630/v1662025929/production/designs/34595437_1.jpg", age="4", notes="Digs a lot of tunnels")
mooches = Pet(name="Moochacho Vera", species="dog", photo_url="https://preview.redd.it/f3r6lcq2hj7c1.jpeg?width=216&crop=smart&auto=webp&s=87edfaf079ad035c6a5548de6729527b80087e47", age="2", notes="Loves the homies", available=False)
db.session.add(poncho)
db.session.add(mooches)
db.session.commit()

