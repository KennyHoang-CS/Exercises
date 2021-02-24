from models import User, db, Post, Tag
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

# Add some posts. 
post1 = Post(title="I love cookies", content="Cookies are delicious and sweet!", user_id=1)
post2 = Post(title="Cats or Dogs?", content="asldlksadlsakdsladmasldkmasl", user_id=2)
post3 = Post(title="Aliens are coming!", content="Hide your wife(or husband) and kids!", user_id=3)
post4 =  Post(title="Vanilla Icecream?", content="The best flavor there is!", user_id=1)

# Add the posts to session.
db.session.add_all([post1,post2,post3, post4])

# Commit posts in session to database. 
db.session.commit()

# Add some tags.
comedy = Tag(name='comedy')
adventure = Tag(name='adventure')
action = Tag(name='action')
fun = Tag(name='fun')
gibberish = Tag(name='gibberish')
desert = Tag(name='desert')

# Add post-tag relationships to database. 
desert.posts.append(post1)
fun.posts.append(post2)
action.posts.append(post3)
desert.posts.append(post4)
fun.posts.append(post4)

# Add tags to session.
db.session.add_all([comedy, adventure, action, fun, gibberish, desert])

# Commit tags in session to database.
db.session.commit()








