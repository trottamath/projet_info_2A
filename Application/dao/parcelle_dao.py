from typing import Optional
import hashlib

from utils.singleton import Singleton
from dao.db_connection import DBConnection
from objets.zone.parcelle import Parcelle

class ParcelleDAO(metaclass=Singleton):
    """classe ParcelleDAO """

    def create(self, id, id_com ):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO parcelle (id_parc, id_com_limit)"\
                    " VALUES (%(id_parc)s, %(id_com_limit)s) RETURNING parcelle_id",
                    {"id_parc": id, "id_com_limit": id_com})
                res = cursor.fetchone() #facultatif ? 

        return res['parcelle_id']  #??
