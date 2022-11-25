############################### Tests commune_dao ###################################

from dao.commune_dao import CommuneDAO
from dao.parcelle_dao import ParcelleDAO
from dao.commune_commune_dao import CommuneCommuneDAO
from dao.parcelle_commune_dao import ParcelleCommuneDAO
import unittest

class CommuneDAOTest(unittest.TestCase):
    
    def test_nom_commune(self):
        c = CommuneDAO()
        #GIVEN
        res1 = '' ###
        #WHEN
        res2 = c.nom_commune('') ###
        #THEN
        self.assertAlmostEquals(res1, res2)
