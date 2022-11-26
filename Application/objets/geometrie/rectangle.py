"""module rectangle.py pour définir la classe Rectangle
version 1.1
date 18/09/2022
auteur : Jean-Philippe Trotta
"""


class Rectangle():
    """Classe Rectangle
    Attributs :
    -----------
        lat_min : float
        lat_max : float
        long_min : float
        long_max : float

    """

    def __init__(
            self,
            lat_min: float,
            lat_max: float,
            long_min: float,
            long_max: float):
        """constructeur de la classe Rectangle
        Paramètres
        ----------
            lat_min : float
            lat_max : float
            long_min : float
            long_max : float
        """
        self.lat_min = lat_min
        self.lat_max = lat_max
        self.long_min = long_min
        self.long_max = long_max

#    def test_point_inclus ( self, autre_point : Point ) -> bool:  # à supprimer si inutile ailleurs
 #       """teste si un point est inclus dans un rectangle
  #      """
   #     print("test inclusion dans rectangle") # TODO à supprimer à la fin
    # return (autre_point.latitude <= self.lat_max) and (autre_point.latitude
    # >= self.lat_min) and (autre_point.longitude <= self.long_max) and
    # (autre_point.longitude >= self.long_min)

    def test_intersect_rect(self, autre_rect) -> bool:
        """teste si un autre rectangle intersecte celui-ci
        Paramètre :
        -----------
            autre_rect : Rectangle
        """
        # print("test intersection de rectangles") # TODO à supprimer à la fin
        if (autre_rect.long_max < self.long_min) or (autre_rect.long_min > self.long_max) or (
                autre_rect.lat_max < self.lat_min) or (autre_rect.lat_min > self.lat_max):
            return False
        else:
            return True

    def union_rectangle(self, autre_rect):
        """retourne le plus petit rectangle (au sens des latitudes et longitudes extrèmes) qui inclus ce rectangle et un autre rectangle donné
        """
        return Rectangle(
            lat_min=min(
                self.lat_min, autre_rect.lat_min), lat_max=max(
                self.lat_max, autre_rect.lat_max), long_min=min(
                self.long_min, autre_rect.long_min), long_max=max(
                    self.long_max, autre_rect.long_max))

    def sous_ensemble(
            self,
            num_ligne: int,
            num_col: int,
            nb_lignes_tot: int,
            nb_col_tot: int):
        ''' Subdivise le rectangle en lignes et colonnes
        et retourne le sous-rectangle selectionné dans la subdivision
        convention: même numérotation que les listes en partant de 0 pour num_col et num_ligne

        Returns
        -------
            Rectangle
        '''
        pas_long = (self.long_max - self.long_min) / nb_col_tot
        pas_lat = (self.lat_max - self.lat_min) / nb_lignes_tot
        return Rectangle(lat_min=self.lat_min + num_ligne * pas_lat,
                         lat_max=self.lat_min + (num_ligne + 1) * pas_lat,
                         long_min=self.long_min + num_col * pas_long,
                         long_max=self.long_min + (num_col + 1) * pas_long)

    def __str__(self) -> str:
        """affichage"""
        print("rectangle:")
        return "Latitude min : {}; latitude max: {}; longitude min: {}; longitude max: {})".format(
            self.lat_min, self.lat_max, self.long_min, self.long_max)
