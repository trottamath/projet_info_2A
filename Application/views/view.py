"""module view.py pour définir la classe View
version 1.0
date 25/10/2022
auteurs : Fiona Fonkou et Jean-Philippe Trotta
"""
from pprint import pprint
from prompt_toolkit.validation import ValidationError, Validator
from InquirerPy import prompt

from views.session import Session
from service.requete import Requete

class View():
    def __init__(self) -> None:
        '''constructeur'''
        self.__questions = [
            {
                'type': 'input',
                'name': 'id_zone',
                'message':'Quel est l\'identifiant de la zone de référence ?'
            }
        ]


    def display_info(self):
        print(f"Veuillez saisir un identifiant de zone correct (sans guillemets)")

    def make_choice(self):
        answers = prompt(self.__questions)
        pprint(answers)
        Session().id = answers['id_zone']
        dico_requete = {"num": Session().num, "id": Session().id, "date": Session().date}
        pprint(dico_requete)
        Session().list_res = Requete(dico_requete= dico_requete ).Get_or_create() 
        pprint(Session().list_res) 

        from views.start_view import StartView
