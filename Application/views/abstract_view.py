from pprint import pprint

#import regex
from prompt_toolkit.validation import ValidationError, Validator
from InquirerPy import prompt

from views.session import Session
#from service.requete import Requete

class AbstractView():
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'input',
                'name': 'id_zone',
                'message':'Quel est l\'identifiant de la zone de référence ?'
            }
        ]



    def display_info(self):
        print(f"Bonjour {Session().user_name}, veuillez choisir un identifiant de zone correct")

    def make_choice(self):
        answers = prompt(self.__questions)
        pprint(answers)
        Session().id=answers['id_zone']
        dico_requete= {"num":Session().num,"id":Session().id,"date":Session().date}
        Session().list_res = Requete(dico_requete= dico_requete ).Get_or_create()
        pprint(Session().list_res) 

        from views.start_view import StartView

