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
print("ordre clé : id, fuel, medical, technical_issue, diplomatic_level")
for i in readable:
    print(i)

# On choisi un ordre de priorité
ordre_priorite = []
ordre_defaut = ["fuel","medical","technical_issue","diplomatic_level"]
for i in range (1,5):
    choix_ordre = input("""
    priorité numéro {} : fuel, medical, technical_issue ou diplomatic_level 
    
    si c'est mal écrit, l'ordre par défaut sera [fuel, medical, technical_issue, diplomatic_level] : """.format(i))

    ordre_priorite.append(choix_ordre)


# on verifie que les clé soit bien écrite. Si ce n'est pas le cas, on utilisera l'ordre par défaut
    
for i in ordre_priorite:
    if i in ordre_defaut:
        pass
    else:
        ordre_priorite = ordre_defaut

# on attribue un score à chaque avion qui déterminera l'ordre d'attérrissage

avion_score = score(avion,ordre_priorite)
avion_trie = tri_avion(avion_score)
redable = lisibilite(avion_trie)
for i in redable:
    print(i)

# Simulation des atterrissages
tour_actuel = 0
dernier_atterrissage = -5  # Initialement, la piste est libre
avions_en_attente = avion_trie.copy()
avions_atteints = []
avions_disparus_carburant = []

while avions_en_attente and tour_actuel < 1000:  
    tour_actuel += 1
    temps_depuis_dernier = tour_actuel - dernier_atterrissage
    etat_piste = etat_p("occupée", "libre", temps_depuis_dernier)
    
    if etat_piste == "libre" and avions_en_attente:
        # Faire atterrir le prochain avion
        avion_atterri = avions_en_attente.pop(0)
        avions_atteints.append(avion_atterri)
        dernier_atterrissage = tour_actuel
        print(f"Minute {tour_actuel}: Avion {avion_atterri['id']} a atterri (fuel restant: {avion_atterri['fuel']}).")
    else:
        if avions_en_attente:
            print(f"Minute {tour_actuel}: Piste occupée, {len(avions_en_attente)} avions en attente.")
    
    # Simuler la perte de fuel pour les avions en attente
    perte_fuel(avions_en_attente)
    # Vérifier les avions avant suppression
    avions_perdus = [a for a in avions_en_attente if a["fuel"] <= 0]
    if avions_perdus:
        avions_disparus_carburant.extend(avions_perdus)
        compteur_de_mort += len(avions_perdus)
    # Supprimer les avions sans fuel
    avions_en_attente = fuel_avions(avions_en_attente)

print("\n Simulation terminée")
print(f"Avions atterris: {len(avions_atteints)}")
print(f"Avions disparus faute de carburant: {compteur_de_mort}")
print(f"Avions encore en attente: {len(avions_en_attente)}")
if avions_disparus_carburant:
    print(f"IDs des avions disparus: {[a['id'] for a in avions_disparus_carburant]}")
    
    




