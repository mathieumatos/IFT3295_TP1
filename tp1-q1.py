import numpy as np

matchValue = 4
mismatchValue = -4
indelValue = -8

S = "GGTCTGAG"
T = "AAACGA"

rows = len(S)+1
columns = len(T)+1



def matchScore(i,j):
    if S[i-1] == T[j-1]:
        return matchValue

    else:
        return mismatchValue


def findMaxScore(i,j):
    diag = tab[i-1][j-1] + matchScore(i,j)
    up = tab[i-1][j] + indelValue
    left = tab[i][j-1] + indelValue
    maximum = max(diag, up, left)
    if maximum == up:
        maxOrigins = 1
        # maxOrigins.append([i-1,j])
    if maximum == left:
        maxOrigins = -1
        # maxOrigins.append([i,j-1])
    if maximum == diag:
        maxOrigins = 0
        # maxOrigins.append([i-1,j-1])

    backtrackTab[i][j] = maxOrigins
    
    return maximum


######### init du tableau 2d ##########

tab = np.empty((rows,columns), np.int32)
backtrackTab = np.empty((rows,columns), np.int32)

for i in range(rows):
    tab[i][0] = 0
    backtrackTab[i][0] = 1

for j in range(columns):
    tab[0][j] = 0
    backtrackTab[0][j] = -1

#########################################


######### equations de recurence ##########

for x in range(rows-1):
    for y in range(columns-1):
        tab[x+1][y+1] = findMaxScore(x+1, y+1)

###########################################



### Trouver max de la derniere colonne ###

# je sais, ce n'est pas la meilleure pratique, je suis nouveau avec python, je pourrais mettre -inf à la place
tempMaxCol = -99999999
indiceLastCol = -1
for x in range(i): 
    if tempMaxCol <= tab[x][len(T)]:
        tempMaxCol = tab[x][len(T)]
        indiceLastCol = [x,len(T)]


print(tempMaxCol)
print(indiceLastCol)
###########################################



### Trouver max de la derniere colonne ###

# je sais, ce n'est pas la meilleure pratique, je suis nouveau avec python, je pourrais mettre -inf à la place
tempMaxRow = -99999999
indiceLastRow = -1
for x in range(j): 
    if tempMaxRow <= tab[len(S)][x]:
        tempMaxRow = tab[len(S)][x]
        indiceLastRow = [len(S),x]


print(tempMaxRow)
print(indiceLastRow)

###########################################



########## Max Value et son Indice #######

maxLast = max(tempMaxCol, tempMaxRow)
if tempMaxCol > tempMaxRow:
    maxLast = tempMaxCol
    maxIndice = indiceLastCol
elif tempMaxCol < tempMaxRow:
    maxLast = tempMaxRow
    maxIndice = indiceLastRow
else:
    maxLast = tempMaxRow
    if indiceLastCol[1] > indiceLastRow[0]:
        maxIndice = indiceLastCol
    else:
        maxIndice = indiceLastRow

print(maxIndice)

############################################



####### RETRACE ######

width = maxIndice[0]
depth = maxIndice[1]

seqS = ""
seqT = ""

# while ((width != -1) and (depth != -1)):
#     print(str(width)+", "+str(depth))
#     if

while ((width > 0) and (depth > 0)):
    print(str(width)+", "+str(depth))
    if backtrackTab[width][depth] == 0:
        seqS = S[width-1] + seqS
        seqT = T[depth-1] + seqT
        width += -1
        depth += -1
        continue
    if backtrackTab[width][depth] == 1:
        seqS = "-" + seqS
        seqT = T[depth-1] + seqT
        width += -1
        continue
    if backtrackTab[width][depth] == -1:
        seqS = S[width-1] + seqS
        seqT = "-" + seqT
        depth += -1
        continue

print("jusqua 0")
print(seqS)
print(seqT)


tempS = ""
tempT = ""

if width > 0:
    for x in range(width):
        tempS += S[x]
        tempT += "-"

if depth > 0:
    for x in range(depth):
        tempS += "-"
        tempT += T[x]

seqS = tempS + seqS
seqT = tempT + seqT

for x in range()

print(str(width)+", "+str(depth))
print(seqS)
print(seqT)


######################


print(S)
print(T)
print(tab)
print(backtrackTab)

# print(len(backtrackTab[8][6]))
# print(backtrackTab[8][6][1][1])


jo = 5
ni = 3

while ((jo != -1) and (ni != -1)):
    print(str(jo)+", "+str(ni))
    if(jo == 0):
        ni += -1
    elif(ni == 0):
        jo += -1
    else:
        jo += -1
        ni += -1

