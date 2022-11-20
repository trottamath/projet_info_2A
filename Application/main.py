
import dotenv
from views.start_view import StartView
dotenv.load_dotenv()
if __name__ == '__main__':
    #run the start view
    current_view = StartView()

    while current_view:


        current_view.display_info()

        current_view = current_view.make_choice()
        


