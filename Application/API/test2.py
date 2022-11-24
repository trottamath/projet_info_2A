# Import classique
from fastapi import FastAPI
import uvicorn
from service.requete import Requete
#from dao.commune_commune_dao import CommuneCommuneDAO
class Connexion_api():

    #dico_requete = {"num": "1","id": '13207', "date": '2021-10-01'}
    
    def lancer_api(self):
        app = FastAPI()

        # Définition du endpoint qui repond à la méthode GET à l'adresse "/" et qui va retourner la liste des communes contigues à id_zone
        @app.get("/")
        async def get_all_commune(id:str, date:str):
            dico_requete = {"num":"1","id":id,"date":date}
            #dico_requete = {"num": '1',"id": '13207', "date": 'latest'}
            req= Requete(dico_requete)
            print("hello")
            return req.Get_DAO()

        # Lancement de l'application sur le le port 80
        uvicorn.run(app, host="127.0.1.0", port=80)

Connexion_api().lancer_api()

