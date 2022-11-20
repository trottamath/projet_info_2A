from client.telechargement import Telechargement
    
#test pour fonction qui recup url
# t = Telechargement()
# lien_1 = t.generator_link(id_dep="08",date="latest",zonage1="departements", id_zone = None)
# print(lien_1)
# lien_2 = t.generator_link("08","latest","communes", id_zone = "08124")
# print(lien_2)
# lien_3 = t.generator_link(id_dep="08",date="latest",zonage1="france",id_zone=None,zonage2="communes")
# print(lien_3)

#test pour le générateur de chemin : 

#print(generator_path('https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/04/04004/cadastre-04004-communes.json.gz'))

#test fonction telechargement
#download('https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/04/04004/cadastre-04004-communes.json.gz','Application/client/data/communes/communes')
#download('https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/04/04005/cadastre-04005-communes.json.gz','Application/client/data/communes/communes')
#download('https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/04/04006/cadastre-04006-communes.json.gz','Application/client/data/communes/communes')

#lecture du json.gz
dico = Telechargement().read_json('https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/04/04004/cadastre-04004-communes.json.gz','/data/communes/communes')
print(dico) #ok
print(type(dico))