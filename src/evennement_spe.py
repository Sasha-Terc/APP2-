import random
def evennement_spe(hasard):
    hasard = random.randint(1, 20)
    if hasard == 1:
        tech_grav = 20

    if hasard == 5:
        importance_diplo = 20

    if hasard == 10:
        urgence_médicale = 20

    if hasard == 20:
        etat_piste = "innondée"
    return tech_grav, importance_diplo, urgence_médicale, etat_piste