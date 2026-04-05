"""L'objectif de cet APP est de faire atterrir des avions en fonction de divers probleme.
On va donc dans l'ordre, generer des avions, leur attribuer un score d'importance et les faire atterrir
malheuresement c'est possible que des avions ne puissent pas atterrir 
c'est pour ça que bien choisir l'ordre est important """

# on importe les fonction
from generate_random_traffic import generate_random_traffic
from etat_piste import etat_p
from evennement_spe import evennement_spe
from fuel import fuel_avions, perte_fuel
from probleme_tech import prblm_tech
from score import score
from tri_avion import tri_avion
from lisibilite import lisibilite

compteur_de_mort = 0

# on veut choisir le scenario et combien d'avion
scenario = input("""
choisissez votre scenario:
normal (fuel entre 5 et 50, pas de probleme medicaux et technique, probleme diplomatique entre 1 et 5)
medical_crisis ( ajout de probleme medicaux)
technical_failure (ajout de probleme technique)
fuel_crisis (fuel entre 5 et 15)
diplomatic_summit (probleme diplomatique passe entre 3 et 5)

tapez exactement le scenario choisi sinon ça lancera le scenario normal : """)

nombre_avions = int(input("Combien d'avion voulez-vous ? : "))


# maintenant qu'on a les informations necessaire, on peut générer les avions
avion = generate_random_traffic(nombre_avions, scenario = scenario)  

readable = lisibilite(avion)
print("ordre clé : id, fuel, medical, technical_issue, diplomatic_level, arrival_time")
for i in readable:
    print(i)

# On doit trier la liste d'avion en fonction de son score
ordre_priorite = []
for i in range (1,5):
    choix_ordre = input("priorité numéro {} (ecrivez correctement la clé) : ".format(i))
    ordre_priorite.append(choix_ordre)



