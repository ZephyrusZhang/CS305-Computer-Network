import unittest

import requests
import tests.BasicTest


class TestTask5Session(tests.BasicTest.BasicTest):
    def test01TestLogin(self):
        resp = requests.post(self.server_base + "apiv2/login", json={"username": "admin", "password": "admin"})
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.cookies.get("SESSION_KEY"))
        print(resp.cookies)

    def test02TestGetImage(self):
        s = requests.session()
        resp = s.get(self.server_base + "apiv2/getimage")
        self.assertEqual(resp.status_code, 403)

        resp = s.post(self.server_base + "apiv2/login", json={"username": "admin", "password": "admin"})
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.cookies.get("SESSION_KEY"))

        resp = s.get(self.server_base + "apiv2/getimage")
        self.assertEqual(resp.status_code, 200)
        flen = self.assertFileContentEqual('data/test.jpg', resp.content)
        self.assertEqual(int(resp.headers['Content-Length']), flen)
        self.assertIn(resp.headers['Content-Type'], ['image/jpeg', 'image/jpg'])

    def test03TestHEADGetImage(self):
        s = requests.session()
        resp = s.head(self.server_base + "apiv2/getimage")
        self.assertEqual(resp.status_code, 403)

        resp = s.post(self.server_base + "apiv2/login", json={"username": "admin", "password": "admin"})
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.cookies.get("SESSION_KEY"))

        resp = s.get(self.server_base + "apiv2/getimage")
        self.assertEqual(resp.status_code, 200)
        flen = self.assertFileContentEqual('data/test.jpg', resp.content)
        self.assertEqual(int(resp.headers['Content-Length']), flen)
        self.assertIn(resp.headers['Content-Type'], ['image/jpeg', 'image/jpg'])

        resp = s.head(self.server_base + "apiv2/getimage")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(int(resp.headers['Content-Length']), flen)
        self.assertIn(resp.headers['Content-Type'], ['image/jpeg', 'image/jpg'])
        self.assertEqual(resp.content, b'')


if __name__ == '__main__':
    unittest.main()
