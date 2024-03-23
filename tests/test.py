import unittest
from flask import url_for
from flask_testing import TestCase
from app import app, db
from models import User

class TestAuth(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        return app

    def setUp(self):
        db.create_all()
        user = User(username='test_user', email='test_user001gmail.com', password_hash='hashed_password', role='client')
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register(self):
        response = self.client.post(
            url_for('auth.register'),
            data=dict(username='new_user', email='test_user001gmail.com', password='password', confirm_password='password', role='client'),
            follow_redirects=True
        )
        self.assertIn(b'Account created successfully!', response.data)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.post(
            url_for('auth.login'),
            data=dict(username='test_user', password='password'),
            follow_redirects=True
        )
        self.assertIn(b'Login successful!', response.data)
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get(
            url_for('auth.logout'),
            follow_redirects=True
        )
        self.assertIn(b'You have been logged out.', response.data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
