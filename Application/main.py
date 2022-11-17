#copier le code du tp pour lancer le programme dans la console
import dotenv
from views.start_view import StartView
dotenv.load_dotenv()
if __name__ == '__main__':
    #run the start view
    current_view = StartView()

    while current_view:
        # with open('graphical_assets/border.txt','r', encoding="utf-8") as asset:
        #     print(asset.read())

        current_view.display_info()

        current_view = current_view.make_choice()

    # with open('graphical_assets/suprised_pikachu.txt', 'r', encoding="utf-8") as asset:
    #     print(asset.read())