
def etat_p(occupe, libre, temps_depuis_dernier_atterrissage):
    temps_occupation = 5  # La piste reste occupée pendant 5 unités de temps après un atterrissage
    if temps_depuis_dernier_atterrissage < temps_occupation:
        etat_piste = occupe
    else:
        etat_piste = libre
    return etat_piste
    
