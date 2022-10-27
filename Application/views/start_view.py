"""
* Checkbox question example
* run example by typing `python example/checkbox.py` in your console
From : https://github.com/CITGuru/PyInquirer/blob/master/examples/checkbox.py
"""
from pprint import pprint

from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

from prompt_toolkit.validation import Validator, ValidationError
from view.abstract_view import AbstractView
from view.session import Session

TEAM_SELECTION = inquirer.checkbox(
            message="Choisis ta requête"
            ,choices=[
                requete1,
                requete2,
                requete3
            ]
        )


class CheckBoxExampleView(AbstractView):
        
    def display_info(self):
        print(f"Bonjour {Session().user_name}, choisissez la commune à traiter")

    def make_choice(self):
        answers = TEAM_SELECTION.execute()
        pprint(answers)
        from view.start_view import StartView
        return StartView()

