# tests.py

import unittest
from flask import url_for
from flask_testing import TestCase # type: ignore
from app import app

class TestApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_homepage(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the homepage', response.data)

    def test_hello_route(self):
        response = self.client.get(url_for('hello'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, World!', response.data)

    def test_invalid_route(self):
        response = self.client.get('/invalid-route')
        self.assertEqual(response.status_code, 404)

    def test_post_method_not_allowed(self):
        response = self.client.post(url_for('index'))
        self.assertEqual(response.status_code, 405)

if __name__ == '__main__':
    unittest.main()
