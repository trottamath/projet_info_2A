from pprint import pprint

import regex
from prompt_toolkit.validation import ValidationError, Validator
from PyInquirer import prompt

from views.abstract_view import AbstractView
from view.session import Session

class Commune_Parcelle_View(AbstractView):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'input',
                'name': 'identifiant de la commune',
                'message':'quel est l\'identifiant du zonage'
            },
            {
                'type':'input',
                'name':'date',
                'message':'quel est la date correspondant à votre recherche'

            }
        ]

    def display_info(self):
        print(f"Hello {Session().user_name}, veuillez choisr un bon identifiant de commune")

    def make_choice(self):
        answers = prompt(self.__questions)
        pprint(answers)
        from views.start_view import StartView