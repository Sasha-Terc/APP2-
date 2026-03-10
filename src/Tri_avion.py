#code sasha tri avion en fonction du score

def tri_avion(liste_avion_score) :  #trie les avions en fonction de leur score (ordre decroissant)
    n =  len(liste_avion_score)
    for i in range(1,n) :
        key = liste_avion_score[i] 
        j = i-1
        while j >= 0 and liste_avion_score[j] < key :
            liste_avion_score[j+1] = liste_avion_score[j]
            j -= 1
            liste_avion_score[j+1] = key
    return liste_avion_score




