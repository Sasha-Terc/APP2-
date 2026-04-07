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

def fuel_avions(liste):
    Liste1 = [] #liste à récupérer pour la suite du code
    Liste2 = [] #liste pour les stats et voir si ça marche
    compteur = 0 #pour compter le nb d'avions qui n'ont plus de fuel

    for d in liste:
        if "fuel" in d: #on vérifie que la clé existe
            if d["fuel"] <= 0: # <= au cas où il y ait une val négative
                Liste2.append(d) #ajout à la liste des stats
                del d #on suprime totalement la liste
                compteur += 1 #incrementation

            else :
                Liste1.append(d) #ajout à la liste utile

    return compteur, Liste1, Liste2

liste = fuel(5) 
print(liste)  
print(perte_fuel(liste))
        


