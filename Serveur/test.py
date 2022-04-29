import unittest
from main import *

class TestWebservice(unittest.TestCase):
    def test_get_response():
        try:
            test_playlist = get_playlist()
            assert type(test_playlist) is json()     
        except:
            assert False


