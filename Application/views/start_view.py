from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from views.abstract_view import AbstractView
from views.session import Session

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
        self.__questions1 = inquirer.select(
            message=f'Bonjour{Session().user_name}'
            , choices=[
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
        # with open('graphical_assets/banner.txt','r',encoding="utf_8") as asset:
        #     print(asset.read())
        pass
    
    def make_choice(self):
        reponse = self.__questions.execute()
        Session().date=self.__questions1.execute()
        if reponse == 'Aucun':
            pass
        elif reponse == 'Liste des communes limitrophes à une commune donnée':
            Session().num="1"
            #from views.commune_commune_view import Commune_Commune_View
            #return Commune_Commune_View()
        elif reponse == 'Liste des parcelles en bordure d\'une commune donnée':
            Session().num="2"
            #from views.commune_parcelle_view import Commune_Parcelle_View
            #return Commune_Parcelle_View()
        elif reponse == 'Liste des parcelles limitrophe à une parcelle donnée':
            Session().num="3"
        from views.abstract_view import AbstractView
        return AbstractView()

