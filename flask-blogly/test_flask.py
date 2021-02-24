from unittest import TestCase
from app import app
from models import db, User, Post, Tag, PostTag

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_ECHO'] = False 
app.config['TESTING'] = True 
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class UserViewsTestCase(TestCase):
    """ Tests for views for Users. """

    def setUp(self):
        """ Add a sample user. """
        db.drop_all()
        db.create_all()

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


class PostViewsTestCase(TestCase):
    """ Tests views for Posts. """

    def setUp(self):
        """ Add a sample post. """
        db.drop_all()
        db.create_all()

        # Get user sample. 
        User.query.delete()
        user = User(first_name="TestFirstName", last_name="TestLastName", image_url="TestImageUrl")
        db.session.add(user)
        db.session.commit()

        # Add sample post to sample user. 
        Post.query.delete()        
        post = Post(title="TestTitle", content="TestContent", user_id=1)
        db.session.add(post)
        db.session.commit()

    def tearDown(self):
        """ Clear any foul transactions. """
        db.session.rollback()

    def test_list_posts(self):
        """ Does the sample post list contain the initial post under sample user? """
        with app.test_client() as client:
            resp = client.get('/users/1')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('TestTitle', html)

    def test_post_details(self):
        """ Are we able to view sample post details? """
        with app.test_client() as client:
            resp = client.get('/posts/1')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('TestContent', html)

    def test_view_post_form(self):
        """ Are we able to see the post form? """
        with app.test_client() as client:
            resp = client.get('/users/1/posts/new')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Add Post for', html)

    def test_delete_post(self):
        """ Are we able to delete the sample post? """
        with app.test_client() as client:
            d = {"title": "TestTitle", 
                "content": "TestContent", 
                "user_id": 1}
            resp = client.post(f'/posts/1/delete', data=d, follow_redirects=True)
            self.assertEqual(resp.status_code, 200)

            resp = client.get('/users/1')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertNotIn('TestTitle', html)


class TagViewsTestCase(TestCase):
    """ Test views for Tags. """ 
    def setUp(self):
        """ Add a sample user that has a post with tags. """
        db.drop_all()
        db.create_all()

        # Get user sample. 
        User.query.delete()
        user = User(first_name="TestFirstName", last_name="TestLastName", image_url="TestImageUrl")
        db.session.add(user)
        db.session.commit()

        # Add sample post to sample user. 
        Post.query.delete()        
        post = Post(title="TestTitle", content="TestContent", user_id=1)
        db.session.add(post)
        db.session.commit()

        # Add some sample tags.
        comedy = Tag(name='comedy')
        adventure = Tag(name='adventure')
        
        # Add post-tag relationships to database. 
        comedy.posts.append(post)
        adventure.posts.append(post)
        db.session.add_all([comedy, adventure])
        db.session.commit()

    def tearDown(self):
        """ Clear any foul transactions. """
        db.session.rollback()

    def test_list_tags(self):
        """ Does the sample post list contain the comedy and adventure tag? """
        with app.test_client() as client:
            resp = client.get('/posts/1')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('adventure', html)

    def test_edit_post_tags(self):
        """ Are we able to view tags in the edit post form? """
        with app.test_client() as client:
            resp = client.get('/posts/1/edit')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('adventure', html)

    def test_add_tag(self):
        """ Are we able to add a tag? """
        with app.test_client() as client:
            d = {"name": "funny"}
            resp = client.post('/tags/new', data=d, follow_redirects=True)
            self.assertEqual(resp.status_code, 200)

            resp = client.get('/tags')
            self.assertEqual(resp.status_code, 200)
            html = resp.get_data(as_text=True)
            self.assertIn('funny', html)

    def test_add_post_tags(self):
        """ Are we able to view tags under new user posts? """
        with app.test_client() as client:
            resp = client.get('/users/1/posts/new')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('adventure', html)
