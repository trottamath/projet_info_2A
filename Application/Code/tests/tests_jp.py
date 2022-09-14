""" module test_jp
version brouillon
auteur: Jean-Philippe Trotta
date : 10/09/2022
"""

from geometrie.multi_polygone import MultiPolygone
from geometrie.polygone import Polygone
from geometrie.point import Point
from geometrie.rectangle import Rectangle



# erreur d'accès au package geometrie TODO

#test poly
poly1 = Polygone([[5425.25,5545],[654436,25545.444],[5425,5545.3254],[654436.65,25545]])
print(poly1)

poly2=Polygone([[12,322],[4,10],[35,44]])
pt1 = Point([0,0])
pt2 = Point([4,10])
print(poly2.test_sommet(pt2))


#test multipoly
m1 = MultiPolygone([[[1,5545.3254],[654436.65,25545.444],[5425,11]],[[2,25545],[654436.65,25545.444],[5425,5545.3254],[654436.65,25545.444],[5425,22]]])

print(m1)

#test rect
rect1 = Rectangle(lat_min=-1, lat_max=5, long_min=-2, long_max=7)

print(rect1.test_point_inclus(pt1))


print(poly1.rectangle_circonscrit())

#test intersection rectangle polygone
poly3 = Polygone([[-2,2],[0,2],[-2,4],[0,4]]) #true
poly4 = Polygone([[5,4],[7,2],[8,7],[10,5]]) #true
poly5 = Polygone([[10,-1],[10,1],[14,-1],[14,1]]) #false
print(poly5.test_intersect_rect(rect1))

#test point à proximité d'un polygone
print(poly4.test_point_proche (pt1)) #false
pt3 = Point([6,6])
print(poly4.test_point_proche (pt3)) #true

#test polygones proches (version non-symétrique)
poly6 = Polygone([[5,1],[6,1],[6,2]])
print(poly6.test_polyg_proche(poly4)) #false
print(poly4.test_polyg_proche(poly6)) #true (false dans le cas symétrique)

poly7 = Polygone([[4,4],[4,6],[6,6]])
print(poly7.test_polyg_proche(poly4)) #true y compris dans le cas symétrique

#test polygones contigus
poly8 = Polygone([[5,1],[4,4],[4,5],[6,6],[6,1]])
print(poly8.test_polyg_contigu(poly7)) #true

