from models import User, db
from app import app 

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it.  
User.query.delete()

# Add some users.
alan = User(first_name="Alan", last_name="Alda")
joel = User(first_name="Joel", last_name="Burton")
jane = User(first_name="Jane", last_name="Smith")

# Add users to the session.
db.session.add(alan)
db.session.add(joel)
db.session.add(jane)

# Commit the users in session to database.
db.session.commit()
