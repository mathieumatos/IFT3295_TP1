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
    
    return max(diag, up, left)


######### init du tableau 2d ##########

tab = np.empty((rows,columns), np.int32)
backtrackTab = np.empty((rows,columns), np.int32)

for i in range(rows):
    tab[i][0] = 0

for j in range(columns):
    tab[0][j] = 0

#########################################


######### equations de recurence ##########

for x in range(rows-1):
    for y in range(columns-1):
        tab[x+1][y+1] = findMaxScore(x+1, y+1)

###########################################






print(S)
print(T)
print(tab)