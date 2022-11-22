
import dotenv
from views.start_view import StartView
dotenv.load_dotenv()
if __name__ == '__main__':
    #run the start view
    current_view = StartView()

    while current_view:


        current_view.display_info()

        current_view = current_view.make_choice()
        


# la requete 1 fonctionne en latest pour la commune 13207 mais pas pour une code faux par exemple 13400
# exemple de vrai numero de parcelle pour les tests 13001000AB0237