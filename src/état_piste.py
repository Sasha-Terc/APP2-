def etat_p(occupe, libre):
    if avions_aterris == True:
        etat_piste = occupe
    else:
        etat_piste = libre
    return etat_piste