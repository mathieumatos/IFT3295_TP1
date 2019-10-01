import numpy as np
import sys

input = open('reads.fq','r')

def calcScore(S,T):
    matchValue = 4
    mismatchValue = -4
    indelValue = -8


    # T = "TCTAGGCT"
    # S = "GGCTACA"

    print("sequence S = "+str(S))
    print("sequence T = "+str(T))

    rows = len(S)+1
    columns = len(T)+1

    def matchScore(i,j):
        if S[i-1] == T[j-1]:
            return matchValue

        else:
            return mismatchValue


    # FLECHES DE PROVENANCE / RETRACING DANS BACKTRACKTAB
    # DIAG = 0, LEFT = -1, UP = 1

    def findMaxScore(i,j):
        diag = tab[i-1][j-1] + matchScore(i,j)
        up = tab[i-1][j] + indelValue
        left = tab[i][j-1] + indelValue
        maximum = max(diag, up, left)
        if maximum == up:
            maxOrigins = 1
        if maximum == left:
            maxOrigins = -1
        if maximum == diag:
            maxOrigins = 0

        backtrackTab[i][j] = maxOrigins
        
        return maximum


    ################# Initialization des matrices 2d ##################

    tab = np.empty((rows,columns), np.int32)
    backtrackTab = np.empty((rows,columns), np.int32)

    for i in range(rows):
        tab[i][0] = 0
        backtrackTab[i][0] = 1

    for j in range(columns):
        tab[0][j] = 0
        backtrackTab[0][j] = -1

    ####################################################################


    ######### Trouver les valeurs dans le tableau ##########

    for x in range(rows-1):
        for y in range(columns-1):
            tab[x+1][y+1] = findMaxScore(x+1, y+1)

    print(tab)
    print(backtrackTab)

    #########################################################


    #################### Trouver max de la derniere column ######################

    # tempMaxCol = -99999999
    # indiceLastCol = -1
    # for x in range(i): 
    #     if tempMaxCol <= tab[x][len(T)]:
    #         tempMaxCol = tab[x][len(T)]
    #         indiceLastCol = [x,len(T)]


    # print("Maximum value in last column = "+str(tempMaxCol))
    # print("Indice of max value in last column = "+str(indiceLastCol))

    #############################################################################



    ### Trouver max de la derniere row ###

    tempMaxRow = -99999999
    indiceLastRow = -1
    for x in range(j): 
        if tempMaxRow <= tab[len(S)][x]:
            tempMaxRow = tab[len(S)][x]
            indiceLastRow = [len(S),x]


    print("Maximum value in last row = "+str(tempMaxRow))
    print("Indice of max value in last row = "+str(indiceLastRow))

    ###########################################



    ########## Max Value et son Indice #######

    # maxLast = max(tempMaxCol, tempMaxRow)
    # if tempMaxCol > tempMaxRow:
    #     maxLast = tempMaxCol
    #     maxIndice = indiceLastCol
    # elif tempMaxCol < tempMaxRow:
    #     maxLast = tempMaxRow
    #     maxIndice = indiceLastRow
    # else:
    #     maxLast = tempMaxRow
    #     if indiceLastCol[1] > indiceLastRow[0]:
    #         maxIndice = indiceLastCol
    #     else:
    #         maxIndice = indiceLastRow

    # print("Maximum's Point = "+str(maxIndice))

    ############################################



    ########################## RETRACE #############################

    depth = rows-1

    width = columns-1
    print("width = "+str(width)+", depth = "+str(depth))

    seqS = ""
    seqT = ""

    # GGTCTGAG----
    # -----GAAACGA

    print("RETRACING ...")

    while True:
        print("Retracing from point ("+str(depth)+", "+str(width)+")")
        if depth == indiceLastRow[0]:
            if width == indiceLastRow[1]:
                print("Reached Max Point")
                break
        if depth != indiceLastRow[0]:
            seqS = S[depth-1] + seqS
            seqT = "-" + seqT
            depth += -1
        elif width != indiceLastRow[1]:
            seqS = "-" + seqS
            seqT = T[width-1] + seqT
            width += -1
        else:
            print("error, breaking")
            break

    print("S' = "+seqS)
    print("T' = "+seqT)

    while True:
        print("Retracing from point ("+str(depth)+", "+str(width)+")")
        if(depth == 0):
            if(width == 0):
                print("Reached (0, 0)")
                break
        if backtrackTab[depth][width] == 0:
            seqS = S[depth-1] + seqS
            seqT = T[width-1] + seqT
            width += -1
            depth += -1
            continue
        elif backtrackTab[depth][width] == 1:
            seqS = S[depth-1] + seqS
            seqT = "-" + seqT
            depth += -1
            continue
        elif backtrackTab[depth][width] == -1:
            seqS = "-" + seqS
            seqT = T[width-1] + seqT
            width += -1
        else:
            print("Error in either backtrack table or depth/width calculation")
            break

    print("S' = "+seqS)
    print("T' = "+seqT)

    ##################################################################


    ########################### SCORE ############################

    score = 0

    if len(seqS) != len(seqT):
        print("Error calculating score, lengths of sequences not the same")
    else:
        for x in range(len(seqS)):
            if seqS[x] == seqT[x]:
                score += matchValue
                continue
            elif ((seqS[x] == "-") or (seqT[x] == "-")):
                continue
            else:
                score += mismatchValue
                continue

    # print("match value = "+str(matchValue))
    # print("mismatch value = "+str(mismatchValue))
    # print("indel value = "+str(indelValue))
    print("final score = "+str(score)) 
    return score

#############################################################


########################### 20x20 Matrice ############################

readsArray = input.readlines()
seqArray = []

for x in range(len(readsArray)):
    if readsArray[x][0] == "A" or readsArray[x][0] == "T" or readsArray[x][0] == "C" or readsArray[x][0] == "G":
        seqArray.append(readsArray[x][slice((len(readsArray[x])-1))])

l = len(seqArray)

# matrice 20x20 -> scoreArray
scoreArray = np.empty((l,l), np.int32)

for i in range(l):
    for j in range(l):
        scoreArray[i][j] = calcScore(seqArray[i],seqArray[j])

for i in range(l):
    scoreArray[i][i] = 0

print(scoreArray)
    

# print(seqArray)

