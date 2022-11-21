"""module connexion_api.py
version 1.0
date 18/11/2022
auteures : Fiona Fonkou  et Justine Farnarier
"""
# Import classique
from fastapi import FastAPI
import uvicorn
from service.requete import Requete



app = FastAPI()

# Définition du endpoint qui repond à la méthode GET à l'adresse "/" et qui va retourner la liste des communes contigues à id_zone
@app.get("/commune/")
async def get_all_commune(id_com:str, date):
    dico_requete = {"num":1,"id":id_com,"date":date}
    return Requete(dico_requete).Get_Client()


# Définition du endpoint qui repond à la méthode GET à l'adresse "/" et qui va retourner la liste des parcelles en bordure de id_zone
@app.get("/commune/")
async def get_all_commune(id_com:str, date):
    dico_requete = {"num":2,"id":id_com,"date":date}
    return Requete(dico_requete).Get_Client()

# Définition du endpoint qui repond à la méthode GET à l'adresse "/" et qui va retourner la liste des parcelles limitrophes à id_zone
@app.get("/commune/")
async def get_all_commune(id_com:str, date):
    dico_requete = {"num":3,"id":id_com,"date":date}
    return Requete(dico_requete).Get_Client()



# Lancement de l'application sur le le port 80
#if __name__ == "__main__":
uvicorn.run(app, host="127.0.1.0", port=8058)

