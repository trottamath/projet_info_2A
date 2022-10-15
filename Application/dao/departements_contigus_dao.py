import csv

class DepartementsContigusDAO():

    with open('departements_contigus.csv', newline='',encoding='utf-8') as csvfile:
        dep_contig = csv.reader(csvfile, delimiter=';')

