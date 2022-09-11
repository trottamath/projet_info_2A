#extraire sous-chaine de caractères
mot="bonjour"
print(mot[1]+mot[2])

def ident(char:str):
    id=""
    for i in range(5):
        id = id + char[i]
    return id
print(ident("13001543613"))

#json
data={"typ":"feature", "id":"01001","geom":{"typ":"polygone", "coord":[[[5,1],[4,4],[4,5],[6,6],[6,1]]]}}
print(data["geom"]["coord"])
