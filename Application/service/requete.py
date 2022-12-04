"""module requete.py pour définir la classe Requete
version 1.0
date 20/10/2022
auteurs : Jean-Philippe Trotta et Eva Puchalski
"""
from dao.commune_commune_dao import CommuneCommuneDAO
from dao.parcelle_dao import ParcelleDAO
from dao.commune_dao import CommuneDAO
from dao.parcelle_commune_dao import ParcelleCommuneDAO

from client.lien_service import LienService
from objets.zone.zonage import Zonage
from objets.zone.departement import Departement
from service.instanciation import Instanciation
from client.telechargement import Telechargement


class Requete ():
    """Classe qui lie le Service à la DAO : envoie de la requête
    à la DAO, et récupération du résultat"""

    def __init__(self, dico_requete: dict):
        """
        Parametres:
        -----------
            dico_requete: dict
                les clées de ce dictionnaire sont
                num : str
                    numero de la requete (1 ou 2 dans le cas de l'appel à la DAO)
                    "1" pour les communes contigües à la commune donnée
                    "2" pour les parcelles en limite de la commune donnée
                    "3" pour les parcelles contigües à la parcelle donnée
                id : str
                    identifiant du zonage donnée
                date : str
                    date du fichier cadatral de référence
                """
        self.dico_requete = dico_requete

        #modification de la date "latest"
        if self.dico_requete["date"] == "latest":
            date =Telechargement(id_zone1=self.dico_requete["id"]).date
            self.dico_requete["date"] = date


    def ident_dep(self):
        '''extrait les 2 ou 3 premiers caractères d'un identifiant
         de zonage pour donner celui du département'''
        id = self.dico_requete["id"]
        id_dep = id[0] + id[1]
        if id_dep == "97":
            id_dep = id_dep + id[2]
        return id_dep

    def Get_DAO(self) -> list[str]:
        """pour demander le resultat à la DAO qui va interroger la base de données"""
        res = None
        # voisines communes à une voisine donnée
        if self.dico_requete["num"] == "1":
            res = CommuneCommuneDAO().recherche_com(
                self.dico_requete["id"], self.dico_requete["date"])

        # parcelles en bordure d'une commune donnée
        elif self.dico_requete["num"] == "2":
            res = ParcelleDAO().research_all_lim(self.dico_requete["id"])

        return res

    # amélioration possible : faire une classe abstraite 
    # puis une classe par requète pour éviter les if / else 
    def Get_Client(self) -> list[str]:
        """pour déterminer le résultat de requête en interaction avec le Client
        et les méthodes de la couche Objets"""
        print(self.dico_requete)
        if self.dico_requete["num"] == "1":
            # l'identifiant de la commune d'intérêt
            id_com = self.dico_requete["id"]
            id_dep = self.ident_dep()  #l'identifiant du département de la commune
            # la liste des id de départements limitrophes
            list_dep = Departement(id_dep=id_dep).dep_contig()

            list_com = Instanciation(
                zonage1="departements",
                id1=id_dep,
                zonage2="communes",
                date=self.dico_requete["date"]).instancier_zonage() #liste des communes du département

            com1 = "Si ce message s'affiche, le code de le commune saisie est faux"
            for commune in list_com:
                if commune.id == id_com:
                    com1 = commune  # commune d'intérêt

            for id_dep in list_dep:
                # concaténation avec les listes de communes des départements
                # limitrophes

                autre_list_com = Instanciation(
                    zonage1="departements",
                    id1=id_dep,
                    zonage2="communes",
                    date=self.dico_requete["date"]).instancier_zonage()
                
                list_com = [*list_com, *autre_list_com]  # concaténation

            list_id_com_contig = []
            for commune in list_com:
                if commune.id != id_com and com1.test_zone_contigu(
                        commune):
                    list_id_com_contig.append(commune.id)

            # enregistrement dans la base de données
            CommuneCommuneDAO().create_all(id_com1=id_com, list_id_com2=list_id_com_contig,
                                           date=self.dico_requete["date"])
            
            CommuneDAO().ajout_commune(id_com= id_com, nom_commune= com1.nom)

            return list_id_com_contig

        elif self.dico_requete["num"] == "2":

            # l'identifiant de la commune d'intérêt
            id_com = self.dico_requete["id"]
            commune = Instanciation(
                zonage1="communes",
                id1=id_com,
                zonage2="communes",
                date=self.dico_requete["date"]).instancier_zonage()
            list_parc = Instanciation(
                zonage1="communes",
                id1=id_com,
                zonage2="parcelles",
                date=self.dico_requete["date"]).instancier_zonage()
            list_id_parc_lim = []
            for parcel in list_parc:
                if parcel.test_zone_contigu(macro_zone=commune[0]):
                    list_id_parc_lim.append(parcel.id)

            # enregistrement dans la base de données
            ParcelleDAO().ajout_liste_parc(list_id_parc=list_id_parc_lim)

            return list_id_parc_lim

        elif self.dico_requete["num"] == "3":
            # l'identifiant de la parcelle d'intérêt
            id_parc = self.dico_requete["id"]
            # identifiant de la commune de cette parcelle
            id_com = id_parc[0:5]
            # recherche des parcelles en limites de cette commune
            requete2_com = Requete(
                dico_requete={
                    "num": "2",
                    "id": id_com,
                    "date": self.dico_requete["date"]})
            if requete2_com.Get_DAO() != [] and requete2_com.Get_DAO() is not None:
                list_id_parc_lim = requete2_com.Get_DAO()
            else:
                list_id_parc_lim = requete2_com.Get_Client()
            # liste de toutes les parcelles de cette commune :
            liste_parc_com1 = Instanciation(
                zonage1="communes",
                id1=id_com,
                zonage2="parcelles",
                date=self.dico_requete["date"]).instancier_zonage()
            for parcel in liste_parc_com1:
                if parcel.id == id_parc:
                    parcel1 = parcel  # parcelle d'intérêt

            # il ne reste que les parcelles contiües à la parcelle donnée au
            #   sein de sa commmune
            liste_parc_com1 = parcel1.ss_list_contig(
                list_zones=liste_parc_com1)

            test_lim = False
            for id in list_id_parc_lim:
                if id == id_parc:
                    test_lim = True
            if test_lim:  # si la parcelle d'intérêt est en limite de sa commune
                requete1_com = Requete(
                    dico_requete={
                        "num": "1",
                        "id": id_com,
                        "date": self.dico_requete["date"]})  # recherche des communes limitrophes
                list_id_com_contig = []
                if requete1_com.Get_DAO() != [] and requete1_com.Get_DAO() is not None:
                    list_id_com_contig = requete1_com.Get_DAO()
                else:
                    list_id_com_contig = requete1_com.Get_Client()

                if list_id_com_contig != [] and list_id_com_contig is not None:
                    for id_com2 in list_id_com_contig:  # pour chaque commune contigüe
                        # recherche des parcelles en limite 
                        #   de la commune contigüe
                        requete2_com2 = Requete(
                            dico_requete={
                                "num": "2",
                                "id": id_com2,
                                "date": self.dico_requete["date"]})
                        if requete2_com2.Get_DAO() != [] and requete2_com.Get_DAO() is not None:
                            list_id_parc_lim2 = requete2_com2.Get_DAO()
                        else:
                            list_id_parc_lim2 = requete2_com2.Get_Client()
                        # liste des parcelles de la commune voisine :
                        liste_parc_com2 = Instanciation(
                            zonage1="communes",
                            id1=id_com2,
                            zonage2="parcelles",
                            date=self.dico_requete["date"]).instancier_zonage()
                        liste_parc_lim2 = []
                        for parc2 in liste_parc_com2:
                            for id in list_id_parc_lim2:
                                if id == parc2.id:  # si c'est une parcelle en 
                                    #limite de la commune voisine
                                    liste_parc_lim2.append(parc2)
                        # restriction aux parcelles contigües avec la parcelle
                        # d'intéret
                        list_parc_contig2 = parcel1.ss_list_contig(
                            list_zones=liste_parc_lim2)
                        liste_parc_com1 = liste_parc_com1 + list_parc_contig2

            list_id_parc_contig = [
                liste_parc_com1[i].id for i in range(
                    len(liste_parc_com1))]
            return list_id_parc_contig


    def Get_or_create(self) -> list[str]:
        
        if self.Get_DAO() is not None and self.Get_DAO() != []:
            return self.Get_DAO()
        else:
            return self.Get_Client()

    # prévoir de retourner un message d'erreur exploitable par la couche
    # controler si la requète n'est pas valide par exemple pour un
    # identifiant de commune inconnue

############# tests

#req= Requete(dico_requete={"num":"1","id":"13207","date":"latest"})
# print(req.Get_Client()) # donne ['13201','13206','13208']
# print(req.Get_DAO()) #None  (encore un pb de DAO)


# Test pour le requete 2 latest et la commune 13207, les parcelles en
# limites sont:
list_parc_lim13207 = ['132078290I0071',
                      '132078290I0070',
                      '132078290I0069',
                      '132078300A0180',
                      '132078300A0178',
                      '132078300B0005',
                      '132078300B0001',
                      '132078300E0003',
                      '132078300E0007',
                      '132078300E0006',
                      '132078300K0130',
                      '132078300K0151',
                      '132078300L0001',
                      '132078300L0004',
                      '132078300L0182',
                      '132078300L0003',
                      '132078320A0032',
                      '132078320A0069',
                      '132078320A0068',
                      '132078320A0020',
                      '132078320A0008',
                      '132078320A0055',
                      '132078320A0026',
                      '132078320A0039',
                      '132078320A0024',
                      '132078320A0023',
                      '132078320A0002',
                      '132078320C0001',
                      '132078320C0008',
                      '132078320C0006',
                      '132078320C0005',
                      '132078330A0174',
                      '132078330A0198',
                      '132078330B0169',
                      '132078330B0168',
                      '132078330B0167',
                      '132078330B0047',
                      '132078330B0046',
                      '132078330B0045',
                      '132078330B0044',
                      '132078330B0043',
                      '132078330B0166',
                      '132078330H0048',
                      '132078330I0002',
                      '132078330I0001',
                      '132078330I0004',
                      '132078330K0132',
                      '132078330L0054',
                      '132078330M0127',
                      '132078350C0006',
                      '132078350D0007']

# pour l'instant, en latest, la requete 3 (en masquant la dao à corriger), réponds que la parcelle 132078290I0071 n'a que 2 parcelles contigües qui sont:
# ['132078290I0070','132078290K0032'] alors qu'elle est en limite de commune, il devrait y en avoir qui ne commencent pas par "13207" (à vérifier )



# exemple pour la requête 3 avec une parcelle : 831200000B0632 est contigüe à :
parc_cont831200000B0632 = ['831200000B0616',
                           '831200000B0626',
                           '831200000B0637',
                           '831200000B0634',
                           '831200000B0639',
                           '831200000B0628',
                           '831200000B0630',
                           '831200000B0633']



