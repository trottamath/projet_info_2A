from dao.commune_dao import CommuneDAO
from dao.parcelle_dao import ParcelleDAO
from dao.commune_commune_dao import CommuneCommuneDAO
from dao.parcelle_commune_dao import ParcelleCommuneDAO


############################### Tests commune_dao ###################################

#c = CommuneDAO()

#print(c.recherche_commune(id_com="13207"))

#### test ajout_commune : OK
#c.ajout_commune('33000', 'Bordeaux')
#c.ajout_commune('39000', 'LONS-LE-SAUNIER')
#print(c.recherche_commune(id_com="83000")) 

#### test nom_commune : OK
#print(c.nom_commune('35170'))
#print(c.nom_communes('35000'))

#### test recherche_commune : OK
#print(c.recherche_commune('45678'))
#print(c.recherche_commune('84000'))

#### test suppression commune : OK
#c.suppression_commune('83000')


############################### Tests parcelle_dao ###################################

#p = ParcelleDAO()

#print(p.recherche_parcelle(id_parc="132078290I0071"))
#print(p.research_all_lim(id_com_limit="13207")) #ne fonctionne pas ?

# test recherche_parcelle : OK
#print(p.recherche_parcelle('50250AZ4'))

#### test suppression_parcelle : OK
#p.suppression_parcelle('45678UY')

#### test ajout_parcelle : OK
#p.ajout_parcelle('14302B6')

#### test research_all_lim
#print(p.research_all_lim('13207'))

#### test ajout_liste_parc :OK
#p.ajout_liste_parc(['AAAAAAA','1111111'])


############################### Tests commune_commune_dao ###################################

#cc = CommuneCommuneDAO()

#### test recherche : OK

#print(cc.recherche_com(id_com="13207", date="latest")) #n'a pas afficher de contenu autre que None TODO
#print(cc.recherche('13207', '13201', 'latest'))

#### test recherche_com : OK
#print(cc.recherche_com('13207', 'latest'))


#### test create : OK
#cc.create('10101', '10102', 'latest')

#### test create_all : OK
#cc.create_all('1111',['222222','333333','44444'], 'latest')


############################### Tests parcelle_commune_dao ###################################

#pc = ParcelleCommuneDAO()

#### test recherche_unit : OK
#print(pc.recherche_unit('132078290I0071', '13207', 'latest'))

#### test create : OK
#pc.create('111111', '22222', 'latest')

#### test create_all : OK
#pc.create_all('11111',['2222','33333','44444'], 'latest')