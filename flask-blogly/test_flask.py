from unittest import TestCase
from app import app
from models import db, User

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_ECHO'] = False 
app.config['TESTING'] = True 
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class UserViewsTestCase(TestCase):
    """ Tests for views for Pets. """

    def setUp(self):
        """ Add a sample user. """

        User.query.delete()

        user = User(first_name="TestFirstName", last_name="TestLastName", image_url="TestImageUrl")
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id
        self.first_name = user.first_name
        self.last_name = user.last_name

    def tearDown(self):
        """ Clean up any foul transaction. """

        db.session.rollback()

    def test_list_users(self):
        """ The list should only have one initial user. """
        with app.test_client() as client:
            resp = client.get('/users')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('TestFirstName', html)

    def test_show_user(self):
        """ Is the user details able to be viewed? """
        with app.test_client() as client:
            resp = client.get(f'users/{self.user_id}')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn(f'<p>{self.first_name}', html)

    def test_add_user(self):
        """ Are we able to add a user? """
        with app.test_client() as client:
            d = {"first_name": "TestFirstName2",
                "last_name": "TestLastName2",
                "image_url": "TestImageUrl2"}
            resp = client.post('/users/new', data=d, follow_redirects=True)
        
            self.assertEqual(resp.status_code, 200)
            
            resp = client.get('/users')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('TestFirstName2', html)

    def test_user_delete(self):
        """ Are we able to delete our initial user? """
        with app.test_client() as client:
            d = {"first_name": "TestFirstName", 
                "last_name": "TestLastName", 
                "image_url": "TestImageUrl"}
            resp = client.post(f'/users/{self.user_id}/delete', data=d, follow_redirects=True)
            self.assertEqual(resp.status_code, 200)

            resp = client.get('/users')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertNotIn('TestFirstName', html)