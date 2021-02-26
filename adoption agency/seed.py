from models import Pet, db
from app import app 

# Create all tables
db.drop_all()
db.create_all()

# IF pets table isn't empty, empty it. 
cat = Pet(name="Timmy", species="Cat", photo_url="https://freepngimg.com/thumb/cat/19-cat-png-image-download-picture-kitten-thumb.png")
dog = Pet(name="Spiky", species="Dog", photo_url="https://directpetsuppliesperth.com.au/image/cache/catalog/catalog/Category%20Pics/DOG-200x200.jpg")
porcupine = Pet(name="Robert", species="Porcupine", photo_url="https://gifts.worldwildlife.org/gift-center/Images/multistepcart/cart-Capuchin-Monkey-photo.jpg")

db.session.add_all([cat, dog, porcupine])
db.session.commit()