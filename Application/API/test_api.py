# Import classique
from fastapi import FastAPI
import uvicorn
#from service.requete import Requete

class Connexion_api():

    communes = {"id_commune": ["40001","40002","40003"], "nom_commune": ["Paris","Rennes","Bruz"]}
    
    def lancer_api(self):
        app = FastAPI()

        # Définition du endpoint qui repond à la méthode GET à l'adresse "/" et qui va retourner la liste des communes contigues à id_zone
        @app.get("/commune_commune/")
        async def get_all_commune(id_comm : str):
            return(self.communes["id_commune"])#id_com:str, date:str):
            """dico_requete = {"num":"1","id":id_com,"date":date}
            return Requete(dico_requete).Get_Client()


        # Définition du endpoint qui repond à la méthode GET à l'adresse "/" et qui va retourner la liste des parcelles en bordure de id_zone
        @app.get("/commune_parcelle/")
        async def get_all_commune(id_com:str, date):
            dico_requete = {"num":"2","id":id_com,"date":date}
            return Requete(dico_requete).Get_Client()

        # Définition du endpoint qui repond à la méthode GET à l'adresse "/" et qui va retourner la liste des parcelles limitrophes à id_zone
        @app.get("/parcelle_parcelle/")
        async def get_all_commune(id_com:str, date):
            dico_requete = {"num":"3","id":id_com,"date":date}
            return Requete(dico_requete).Get_Client()
        """



        # Lancement de l'application sur le le port 80
        uvicorn.run(app, host="127.0.1.0", port=80)

Connexion_api().lancer_api()