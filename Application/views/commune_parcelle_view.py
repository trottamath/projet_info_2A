from pprint import pprint

import regex
from prompt_toolkit.validation import ValidationError, Validator
from PyInquirer import prompt

from views.abstract_view import AbstractView
from views.session import Session
from service.requete import Requete

class Commune_Parcelle_View(AbstractView):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'input',
                'name': 'id_commune',
                'message':'quel est l\'identifiant de la zone de référence'
            }
        ]



    def display_info(self):
        print(f"Hello {Session().user_name}, veuillez choisr un bon identifiant de commune")

    def make_choice(self):
        answers = prompt(self.__questions)
        pprint(answers)
        Session().id=answers['id_commune']
        dico_requete= {"num":Session().num,"id":Session().id,"date":Session().date}
        Session().list_res = Requete(dico_requete= dico_requete ).Get_or_create()
        pprint(Session().list_res) 

        from views.start_view import StartView