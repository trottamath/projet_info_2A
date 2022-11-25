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
        @app.get("/commune_commune/{id_com}")
        async def get_all_commune(id_com):
            dico_requete = {"num": '1', "id": id_com, "date": 'latest'}
            req = Requete(dico_requete)
            return req.Get_DAO()

        # Lancement de l'application sur le le port 80
        uvicorn.run(app, host= "127.0.1.0", port= 80)

        #lien à saisir sur le web :
        #http://127.0.1.0/commune_commune/?id_com=13207
        #http://127.0.1.0/docs#/default/get_all_commune_commune_commune__id_com__get
        #entrer l'id dans le path
        # Définition du endpoint qui repond à la méthode GET à l'adresse "/" et qui va retourner la liste des parcelles en bordure de id_zone
        @app.get("/commune_parcelle/{id_com}")
        async def get_all(id_com):
            dico_requete = {"num": "2", "id": id_com, "date": 'latest'}
            #return Requete(dico_requete).Get_Client()
            req= Requete(dico_requete)
            return req.Get_DAO()
        
        uvicorn.run(app, host= "127.0.1.0", port= 80)

        #http://127.0.1.0/docs#/default/get_all_commune_parcelle__id_com__get

        # Définition du endpoint qui repond à la méthode GET à l'adresse "/" et qui va retourner la liste des parcelles limitrophes à id_zone
        @app.get("/parcelle_parcelle/")
        async def get_all_commune(id_com: str, date):
            dico_requete = {"num": "3", "id": id_com, "date": date}
            return Requete(dico_requete).Get_Client()

Connexion_api().lancer_api()
