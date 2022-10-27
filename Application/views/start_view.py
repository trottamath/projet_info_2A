from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstract_view import AbstractView
from view.session import Session

class StartView(AbstractView):

    def __init__(self):
        self.__questions = inquirer.select(
            message=f'Bonjour{Session().user_name}'
            , choices=[
                Choice('Liste des communes limitrophes à une commune donnée')
                ,Choice('Liste des parcelles en bordure d\'une commune donnée')
                ,Choice('Liste des parcelles limitrophes à une parcelle donnée')
                ,Choice('Aucun')
            ]
        )
    def display_info(self):
        with open('graphical_assets/banner.txt','r',encoding="utf_8") as asset:
            print(asset.read())
    
    def make_choice(self):
        reponse = self.__questions.execute()
        if reponse == 'Aucun':
            pass
        elif reponse == 'Liste des communes limitrophes à une commune donnée':
            num="1"
            from views.commune_commune_view import Commune_Commune_View
            return Commune_Commune_View()
        elif reponse == 'Liste des parcelles en bordure d\'une commune donnée':
            num="2"
            from views.commune_parcelle_view import Commune_Parcelle_View
            return Commune_Parcelle_View()
        elif reponse == 'Liste des parcelles limitrophe à une parcelle donnée':
            num="3"
            from views.parcelle_parcelle_view import Parcelle_Parcelle_View
            return Parcelle_Parcelle_View()

