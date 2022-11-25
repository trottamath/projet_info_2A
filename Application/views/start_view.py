"""module start_view.py pour définir la classe StartView
version 1.0
date 25/10/2022
auteurs : Fiona Fonkou et Jean-Philippe Trotta
"""
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from views.abstract_view import AbstractView
from views.session import Session

class StartView(AbstractView):

    def __init__(self):
        self.__questions = inquirer.select(
            message = f'Bonjour {Session().user_name}, choisissez une requête :'
            , choices = [
                Choice('Liste des communes limitrophes à une commune donnée')
                ,Choice('Liste des parcelles en bordure d\'une commune donnée')
                ,Choice('Liste des parcelles limitrophes à une parcelle donnée')
                ,Choice('Quitter')  #attention lorsqu'on choisi quitter, ça continue qd même!!!
            ]
        )
        self.__questions1 = inquirer.select(
            message = f'Choissez une date ou latest :'
            , choices = [
                Choice('2019-01-01')
                ,Choice('2019-04-01')
                ,Choice('2019-07-01')
                ,Choice('2019-10-01')
                ,Choice('2020-01-01')
                ,Choice('2020-07-01')
                ,Choice('2020-10-01')
                ,Choice('2021-02-01')
                ,Choice('2021-04-01')
                ,Choice('2021-07-01')
                ,Choice('2021-10-01')
                ,Choice('2022-01-01')
                ,Choice('2022-04-01')
                ,Choice('2022-07-01')

                ,Choice('latest')
            ]
        )
    def display_info(self):
        pass
    
    def make_choice(self):
        reponse = self.__questions.execute()
        Session().date = self.__questions1.execute()
        if reponse == 'Quitter':
            pass
        elif reponse == 'Liste des communes limitrophes à une commune donnée':
            Session().num = "1"

        elif reponse == 'Liste des parcelles en bordure d\'une commune donnée':
            Session().num = "2"

        elif reponse == 'Liste des parcelles limitrophes à une parcelle donnée':
            Session().num = "3"
        from views.abstract_view import AbstractView
        return AbstractView()
