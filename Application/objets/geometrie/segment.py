"""module segment.py pour définir la classe Segment
version 1.0
date 18/09/2022
auteur : Jean-Philippe Trotta
"""
from objets.geometrie.point import Point


class Segment():
    """Classe Segment
    Attributs :
    -----------
        point1 : Point
        point2 : Point

    """

    def __init__(self, point1: Point, point2: Point):
        """constructeur de la classe segment
        """
        self.point1 = point1
        self.point2 = point2

    def test_egal(self, autre_segment) -> bool:
        """test d'égalité avec un 2ème segment
        Parametre:
        ----------
            autre_segment : Segment
        """
        # print("test d'égalité de segment") # TODO à supprimer à la fin
        return (
            (
                self.point1.test_egal(
                    autre_segment.point1)) and (
                self.point2.test_egal(
                    autre_segment.point2))) or (
                        (self.point1.test_egal(
                            autre_segment.point2)) and (
                                self.point2.test_egal(
                                    autre_segment.point1)))

    def __str__(self) -> str:
        """affichage
        """
        print("Segment:")
        return "[ {} ; {} ]".format(str(self.point1), str(self.point2))
