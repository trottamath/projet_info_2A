############################### Tests commune_dao ###################################

from dao.commune_dao import CommuneDAO
import unittest

class CommuneDAOTest(unittest.TestCase):
    
    def test_nom_commune(self):
        c = CommuneDAO()
        res1 = c.nom_com # ??
