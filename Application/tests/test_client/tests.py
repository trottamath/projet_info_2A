'''module system'''

from client.departementscommunes import DepartementsCommunes
from client.departementsparcelles import DepartementsParcelles
from client.communescommunes import CommunesCommunes
from client.communesparcelles import CommunesParcelles
from client.multiplesdepartements import MultiplesDepartements


#Test pour la classe DepartementsCommunes

#D = DepartementsCommunes()
#print(D.count())
#D.delete_older_file()

#Test pour la classe DepartementsParcelles 

#D = DepartementsParcelles()
#print(D.count())
#D.delete_older_file()

#Test pour la classe CommunesParcelles

#D = CommunesParcelles()
#print(D.count())
#D.delete_older_file()

#Test pour la classe CommunesCommunes 

#D = CommunesCommunes()
#print(D.count())
#D.delete_older_file()

#Test pour la classe MultiplesDepartements

T = MultiplesDepartements()
U = ['06','972']
T.certains_departements_communes(U)