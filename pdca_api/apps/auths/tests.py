from django.test import TestCase


class MyTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_2_func(self):
        print("test_2_func")

    def test_1_func(self):
        print("test_1_func")

