import random
from trie_par_selection import selection_sort
def fuel(nb_avion):
    L_fuel = []
    for i in range (0, nb_avion):
        fuel = random.randint(5,40)
        L_fuel.append(fuel)
    selection_sort(L_fuel)
    return L_fuel

def perte_fuel(liste):
    for i in range(len(liste)):
        liste[i] -= 1
    return liste

def fuel_avions(liste):
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
        


