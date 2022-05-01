import unittest
from fastapi.testclient import TestClient
from audiodb import get_artiste
from main import *


class TestWebservice(unittest.TestCase):
    def test_get_artiste(self):
        """ Permet de vérifier la sortie de la fonction get_artiste()
        """
        idArtist = "118294"
        try:
            test_artiste = get_artiste("Tryo")[0]['artists'][0]['idArtist'] 
            self.assertEqual(test_artiste,idArtist)      
        except:
            assert False
 
    def test_read_main(self):
        """Teste le bon fonctionnement
        """
        client = TestClient(app)
        response = client.get("/")
        self.assertEqual(response.status_code,200) 
    


 

