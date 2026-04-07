from lisibilite import lisibilite

def score(dico,liste):
    score = 0
    multiplicateur = [2,1.5,1,0.75]
    l_fuel = []
    l_medical = []
    l_technical_issue = []
    l_diplomatic_level = []
    l_score = []
    for i in range (4):
        if liste[i] == "fuel":
            for j in range (len(dico)):
                if  0 < dico[j]["fuel"] < 10 :
                    score = 20*multiplicateur[i]
                    l_fuel.append(score)
                    score = 0
                elif 10 < dico[j]["fuel"] < 20 :
                    score = 15*multiplicateur[i]
                    l_fuel.append(score)
                    score = 0
                elif 20 < dico[j]["fuel"] < 30 :
                    score = 10*multiplicateur[i]
                    l_fuel.append(score)
                    score = 0
                elif 30 < dico[j]["fuel"] < 40 :
                    score = 5*multiplicateur[i]
                    l_fuel.append(score)
                    score = 0
                else:
                    l_fuel.append(score)
        elif liste[i] == "medical":
            for j in range (len(dico)):
                if dico [j]["medical"] == True:
                    score = 20*multiplicateur[i]
                    l_medical.append(score)
                    score = 0
                else:
                    l_medical.append(0)
        elif liste[i] == "technical_issue":
            for j in range (len(dico)):
                if dico [j]["technical_issue"] == True:
                    score = 20*multiplicateur[i]
                    l_technical_issue.append(score)
                    score = 0
                else:
                    l_technical_issue.append(0)
        else:
            for j in range(len(dico)):
                if dico[j]["diplomatic_level"] == 5:
                    score = 20 * multiplicateur[i]
                    l_diplomatic_level.append(score)
                    score = 0
                elif dico[j]["diplomatic_level"] == 4:
                    score = 15 * multiplicateur[i]
                    l_diplomatic_level.append(score)
                    score = 0
                elif dico[j]["diplomatic_level"] == 3:
                    score = 10 * multiplicateur[i]
                    l_diplomatic_level.append(score)
                    score = 0
                elif dico[j]["diplomatic_level"] == 2:
                    score = 20 * multiplicateur[i]
                    l_diplomatic_level.append(score)
                    score = 0
                else:
                    l_diplomatic_level.append(score)
    # maintenant on va additionner les listes entre elles pour avoir le score total
    for i in range (len(l_fuel)):  # peu importe la liste, c'est la même longueur           
        score = l_fuel[i] + l_medical[i] + l_technical_issue[i] + l_diplomatic_level[i]
        l_score.append(score)
        score = 0
    # maintenant on veut attribuer le score à chaque avion
    for i in range(len(dico)):
        dico[i]["score"] = l_score[i]

    return dico

avion = [
    {"id": "AF342", "fuel": 18, "medical": False, "technical_issue": False, "diplomatic_level": 2},
    {"id": "LH908", "fuel": 25, "medical": False, "technical_issue": True,  "diplomatic_level": 1},
    {"id": "BA117", "fuel": 14, "medical": True,  "technical_issue": False, "diplomatic_level": 3},
    {"id": "EK202", "fuel": 40, "medical": False, "technical_issue": False, "diplomatic_level": 5},
    {"id": "AZ721", "fuel": 9,  "medical": False, "technical_issue": False, "diplomatic_level": 1}
]

ordre_defaut = ["fuel","medical","technical_issue","diplomatic_level"]

score_dico = score(avion,ordre_defaut)
readable = lisibilite(score_dico)

for i in readable:
    print(i)


                            


            






    