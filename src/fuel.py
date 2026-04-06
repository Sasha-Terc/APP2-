import random
from trie_par_selection import selection_sort


def fuel(nb_avion):                       # fonction pour tester "perte_fuel"
    L_fuel = []
    for i in range (0, nb_avion):
        fuel = random.randint(5,40)
        L_fuel.append({"fuel":fuel})
    selection_sort(L_fuel,"fuel")
    return L_fuel

def perte_fuel(dico):                    # permet de faire baisser de 1 le carburant de tout les avions
    for i in range(len(liste)):
        dico[i]["fuel"] -= 1
    return liste

def fuel_avions(liste):                   # permet de supprimer les avions sans carburant 
    for i in range(len(liste)):
        if liste[i]["fuel"] <= 0:
            liste.pop(i)
            print(liste)
            return liste
        else :
            continue

liste = fuel(5) 
print(liste)  
print(perte_fuel(liste))
        


