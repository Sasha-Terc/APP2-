import random
from Trie_par_selection import selection_sort
def fuel(nb_avion):
    L_fuel = []
    for i in range (0, nb_avion):
        fuel = random.randint(5,40)
        L_fuel.append(fuel)
    selection_sort(L_fuel)
    return L_fuel

def perte_fuel(liste):
    while liste:
        liste.pop(0)
        for i in range(len(liste)):
            liste[i] -= 1

        nouvelle_liste = []
        for x in liste:
            if x > 0:
                nouvelle_liste.append(x)
        liste = nouvelle_liste


        print(liste)
    return ""

    

liste = fuel(5)   
print(perte_fuel(liste))
        


