import unittest
import os
import sqlite3
import json
from app import app, init_db, DB_NAME, REAL_ADMIN_USER, REAL_ADMIN_PASS

class HoneypotTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.secret_key = 'test_key'
        self.client = app.test_client()
        if os.path.exists(DB_NAME):
            os.remove(DB_NAME)
        init_db()

    def tearDown(self):
        if os.path.exists(DB_NAME):
            os.remove(DB_NAME)

    def test_api_stats_auth(self):
        # 1. Try accessing without login
        response = self.client.get('/api/stats')
        self.assertEqual(response.status_code, 401)

        # 2. Login
        self.client.post('/dashboard-login', data={
            'username': REAL_ADMIN_USER,
            'password': REAL_ADMIN_PASS
        }, follow_redirects=True)

        # 3. Access API
        response = self.client.get('/api/stats')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('total_attacks_today', data)
        self.assertIn('top_attackers', data)

if __name__ == '__main__':
    unittest.main()
