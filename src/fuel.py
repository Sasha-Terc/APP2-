import random
from trie_par_selection import selection_sort


def fuel(nb_avion):                       # fonction pour tester "perte_fuel"
    L_fuel = []
    for i in range (0, nb_avion):
        fuel = random.randint(5,40)
        L_fuel.append({"fuel":fuel})
    selection_sort(L_fuel,"fuel")
    return L_fuel

def perte_fuel(dico):                    # permet de faire baisser de 0.2 le carburant de tout les avions
    for i in dico:                       # Le carburant baisse de 1 à chaque fois qu'un avion se pose (toute les 5min)
        i["fuel"] -= 1
    return dico

def fuel_avions(liste):                   # permet de supprimer les avions sans carburant 
    resultat = []
    for avion in liste:
        if avion["fuel"] > 0:
            resultat.append(avion)
    return resultat
    liste = fuel(5) 



        


