from utils.singleton import Singleton


class Session(metaclass=Singleton):
    def __init__(self):
        """
        Définition des variables que l'on stocke en session
        La syntaxe => ref:type = valeur nous permet de donner le type des variables.
        """
        self.id_utilisateur: int = "2058"
        self.id_requete: int = None
        self.id_commune : int = None
        
       

