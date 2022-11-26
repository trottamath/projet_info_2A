"""module importation.py
version 1.0
date 05/11/2022
auteur : Chloé Contant
"""
from client.telechargement import Telechargement
import requests
from abc import ABC, abstractmethod

# https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/departements/01/cadastre-01-communes.json.gz

url = "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/departements/"


class MultiplesDepartements(Telechargement):

    DEPARTEMENTS = {
        '01': 'Ain',
        '02': 'Aisne',
        '03': 'Allier',
        '04': 'Alpes-de-Haute-Provence',
        '05': 'Hautes-Alpes',
        '06': 'Alpes-Maritimes',
        '07': 'Ardèche',
        '08': 'Ardennes',
        '09': 'Ariège',
        '10': 'Aube',
        '11': 'Aude',
        '12': 'Aveyron',
        '13': 'Bouches-du-Rhône',
        '14': 'Calvados',
        '15': 'Cantal',
        '16': 'Charente',
        '17': 'Charente-Maritime',
        '18': 'Cher',
        '19': 'Corrèze',
        '2A': 'Corse-du-Sud',
        '2B': 'Haute-Corse',
        '21': 'Côte-d\'Or',
        '22': 'Côtes-d\'Armor',
        '23': 'Creuse',
        '24': 'Dordogne',
        '25': 'Doubs',
        '26': 'Drôme',
        '27': 'Eure',
        '28': 'Eure-et-Loir',
        '29': 'Finistère',
        '30': 'Gard',
        '31': 'Haute-Garonne',
        '32': 'Gers',
        '33': 'Gironde',
        '34': 'Hérault',
        '35': 'Ille-et-Vilaine',
        '36': 'Indre',
        '37': 'Indre-et-Loire',
        '38': 'Isère',
        '39': 'Jura',
        '40': 'Landes',
        '41': 'Loir-et-Cher',
        '42': 'Loire',
        '43': 'Haute-Loire',
        '44': 'Loire-Atlantique',
        '45': 'Loiret',
        '46': 'Lot',
        '47': 'Lot-et-Garonne',
        '48': 'Lozère',
        '49': 'Maine-et-Loire',
        '50': 'Manche',
        '51': 'Marne',
        '52': 'Haute-Marne',
        '53': 'Mayenne',
        '54': 'Meurthe-et-Moselle',
        '55': 'Meuse',
        '56': 'Morbihan',
        '57': 'Moselle',
        '58': 'Nièvre',
        '59': 'Nord',
        '60': 'Oise',
        '61': 'Orne',
        '62': 'Pas-de-Calais',
        '63': 'Puy-de-Dôme',
        '64': 'Pyrénées-Atlantiques',
        '65': 'Hautes-Pyrénées',
        '66': 'Pyrénées-Orientales',
        '67': 'Bas-Rhin',
        '68': 'Haut-Rhin',
        '69': 'Rhône',
        '70': 'Haute-Saône',
        '71': 'Saône-et-Loire',
        '72': 'Sarthe',
        '73': 'Savoie',
        '74': 'Haute-Savoie',
        '75': 'Paris',
        '76': 'Seine-Maritime',
        '77': 'Seine-et-Marne',
        '78': 'Yvelines',
        '79': 'Deux-Sèvres',
        '80': 'Somme',
        '81': 'Tarn',
        '82': 'Tarn-et-Garonne',
        '83': 'Var',
        '84': 'Vaucluse',
        '85': 'Vendée',
        '86': 'Vienne',
        '87': 'Haute-Vienne',
        '88': 'Vosges',
        '89': 'Yonne',
        '90': 'Territoire de Belfort',
        '91': 'Essonne',
        '92': 'Hauts-de-Seine',
        '93': 'Seine-Saint-Denis',
        '94': 'Val-de-Marne',
        '95': 'Val-d\'Oise',
        '971': 'Guadeloupe',
        '972': 'Martinique',
        '973': 'Guyane',
        '974': 'La Réunion',
        '976': 'Mayotte',
    }

    def __init__(self, dict_dep: dict = DEPARTEMENTS):
        '''constructeur'''
        self.num_dep = list(dict_dep.keys())
        self.name_dep = list(dict_dep.values())

    def certains_departements(self, liste_dep: list):
        '''Méthode qui télécharge un certain nombre de départements français selon leur identifiant'''
        for i in liste_dep:
            t = Telechargement(
                id_zone1=i,
                date="latest",
                zonage1="departements")
            link = t.generator_link()
            print(link)
            path = t.generator_path()
            print(path)
            t.download()

    def france_entiere(self):
        '''Méthode qui télécharge tous les départements de la France'''

        for i in self.num_dep:
            t = Telechargement(
                id_zone1=i,
                date="latest",
                zonage1="departements")
            link = t.generator_link()
            print(link)
            path = t.generator_path()
            print(path)
            t.download()


############################################################### TEST #####

# test pour certains départements

# T = MultiplesDepartements()
# U = ['02','67','974','25']
# T.certains_departements(U)


# test pour france entière

# T = MultiplesDepartements()
# T.france_entiere()
