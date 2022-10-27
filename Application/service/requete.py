from dao.commune_commune_dao import CommuneCommuneDAO
from dao.parcelle_dao import ParcelleDAO
from dao.commune_dao import CommuneDAO
from dao.parcelle_commune_dao import ParcelleCommuneDAO

from client.lien_service import LienService
from objets.zone.zonage import Zonage
from objets.zone.departement import Departement
from service.instanciation import Instanciation

# quel est l'intérêt de la couche API si nos requête sont gérées ici ?
class Requete ():
    """Classe qui lie le Service à la DAO : envoie de la requête
    à la DAO, et récupération du résultat"""

    def __init__(self, dico_requete:dict) :
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
            

    def Get_DAO(self)->list[str]:
        """pour demander le resultat à la DAO qui va interroger la base de données"""
        if self.dico_requete["num"] == "1" : # voisines communes à une voisine donnée
            res = CommuneCommuneDAO().recherche_com(self.dico_requete["id"], self.dico_requete["date"])
        
        elif self.dico_requete["num"] == "2" : # parcelles en bordure d'une commune donnée
            res = ParcelleDAO().research_all_lim(self.dico_requete["id"])
        
        else:
            res= None

        return res
    
    #faire une classe abstraite puis une classe par requète pour éviter les if else ? TODO
    def Get_Client(self) -> list[str]:
        """pour déterminer le résultat de requête en interaction avec le Client 
        et les méthodes de la couche Objets"""
        if self.dico_requete["num"] == "1" :
            id_com = self.dico_requete["id"] #l'identifiant de la commune d'intérêt
            id_dep = ident_dep(id= id_com) #l'identifiant du département de la commune  TODO vérifier syntaxe staticmethod
            list_dep = Departement(id_dep= id_dep).dep_contig() #la liste des id de départements limitrophes
            list_com = Instanciation(zonage1="departement", id1=id_dep, zonage2="commune", date=self.dico_requete["date"]).instancier_zonage() #liste des communes du département
            
            for commune in list_com:
                if commune.id == id_com:
                    com1= commune #commune d'intérêt

            for id_dep in list_dep:
                # concaténation avec les listes de communes des départements limitrophes
                list_com = list_com + Instanciation(zonage1="departement", id1=id_dep, zonage2="commune", date=self.dico_requete["date"]).instancier_zonage() #concaténation
            
            list_id_com_contig = []
            
            for commune in list_com:
                if commune.id != id_com and com1.test_zone_contigu(commune):
                    list_id_com_contig.append(commune.id)
            
            #enregistrement dans la base de données
            CommuneCommuneDAO().create_all(id_com1= id_com, list_id_com2= list_id_com_contig, date= self.dico_requete["date"])
            CommuneDAO().ajout_commune(id_com= id_com, nom_com= com1.nom)
            
            return list_id_com_contig
        
        if self.dico_requete["num"] == "2" :
            
            id_com = self.dico_requete["id"] #l'identifiant de la commune d'intérêt
            id_dep = ident_dep(id= id_com) #l'identifiant du département de la commune  TODO vérifier syntaxe staticmethod
            commune = Instanciation(zonage1="commune", id1=id_dep, zonage2="commune", date=self.dico_requete["date"]).instancier_zonage()
            list_parc = Instanciation(zonage1="commune", id1=id_dep, zonage2="parcelle", date=self.dico_requete["date"]).instancier_zonage()
            list_id_parc_lim=[]
            for parcel in list_parc:
                if parcel.test_zone_contigu(macro_zone= commune):
                    list_id_parc_lim.append(parcel.id)

            #enregistrement dans la base de données
            ParcelleCommuneDAO().create_all(id_com= id_com, list_id_parc= list_id_parc_lim, date= self.dico_requete["date"] )

            return list_id_parc_lim
        
        if self.dico_requete["num"] == "3" :
            id_parc = self.dico_requete["id"] #l'identifiant de la parcelle d'intérêt
            id_com = ss_str(chaine= id_parc, nbr_caract= 5) #identifiant de la commune de cette parcelle
            #id_dep = ident_dep(id= id_parc)
            requete2_com = Requete(dico_requete= {"num":"2","id":id_com,"date":self.dico_requete["date"]})
            if requete2_com.Get_DAO() != []:
                list_id_parc_lim = requete2_com.Get_DAO()
            else:
                list_id_parc_lim = requete2_com.Get_Client()

            liste_parc_com1 = Instanciation(zonage1="commune", id1=id_com, zonage2="parcelle", date=self.dico_requete["date"]).instancier_zonage()
            for parcel in liste_parc_com1:
                if parcel.id == id_parc:
                    parcel1 = parcel #parcelle d'intérêt
            
            liste_parc_com1 = parcel1.ss_list_contig(list_zones= liste_parc_com1) #il ne reste que les parcelles contiües à la parcelle donnée au sein de sa commmune

            test_lim=False
            for id in list_id_parc_lim:
                if id==id_parc:
                    test=True
            if test: #si la parcelle d'intérêt est en limite de sa commune
                requete1_com = Requete(dico_requete= {"num":"1","id":id_com,"date":self.dico_requete["date"]})
                if requete1_com.Get_DAO() != []:
                    list_id_com_contig = requete1_com.Get_DAO()
                else:
                    list_id_com_contig = requete1_com.Get_Client()
            
                #liste_parc_com2 = []
                for id_com2 in list_id_com_contig: #pour chaque commune contigüe
                    requete2_com2 = Requete(dico_requete= {"num":"2","id":id_com2,"date":self.dico_requete["date"]})
                    if requete2_com2.Get_DAO() != []:
                        list_id_parc_lim2 = requete2_com2.Get_DAO()
                    else:
                        list_id_parc_lim2 = requete2_com2.Get_Client()
                    liste_parc_com2 = Instanciation(zonage1="commune", id1=id_com2, zonage2="parcelle", date=self.dico_requete["date"]).instancier_zonage()
                    liste_parc_lim2 = []
                    for parc2 in liste_parc_com2:
                        for id in list_id_parc_lim2:
                            if id==parc2.id:
                                liste_parc_lim2.append(parc2)
                    liste_parc_com1 =  liste_parc_com1 + parcel1.ss_list_contig(list_zones= liste_parc_lim2)
            
            list_id_parc_contig = [liste_parc_com1[i].id for i in range(len(liste_parc_com1))]
            return list_id_parc_contig





    def Get_or_create(self) ->list[str]:
        if self.Get_DAO()!=None and self.Get_DAO()!=[]: #à vérifier TODO
            return self.Get_DAO()
        else:
            return self.Get_Client()

            



