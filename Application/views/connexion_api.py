#à supprimer

from fastapi import FastAPI 

app = FastAPI()

@app.get("/predict")
def test_zone_contigu(self, macro_zone, liste_reponse) -> list:

    #initialisation de la réponse à retourner 
    reponse = {"success": False}

    #boucle pour retourner la réponse à l'utilisateur 
    if reponse != False:
        return reponse = liste_reponse
    
    