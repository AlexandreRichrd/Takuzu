from operator import le
import dic


def initTakuzuSecret() :
  matrice = list ([ [2, 1, 2, 0],
                    [2, 2, 0, 2],
                    [2, 0, 2, 2],
                    [1, 1, 2, 0]] )
  return matrice

def initTakuzuCorrect () :
  matrice = list ([ [0, 1, 1, 0],
                    [1, 0, 0, 1],
                    [0, 0, 1, 1],
                    [1, 1, 0, 0]] )

  return matrice

def initTakuzuNonCorrect () :
  matrice = list ([ [0, 1, 1, 1],
                    [1, 0, 0, 1],
                    [0, 0, 1, 1],
                    [1, 1, 0, 0]] )
  return matrice

def checkValidity(takuzu):

  #check ligne
  for i in range(len(takuzu)):
    tabCheck = []
    for j in range(len(takuzu)):
      tabCheck.append(takuzu[i][j])
    if(tabCheck.count(0) > 2 or tabCheck.count(1) > 2):
      return False

  #Check colonne
  for i in range(len(takuzu)):
    tabCheck = []
    for j in range(len(takuzu)):
      tabCheck.append(takuzu[j][i])
    if(tabCheck.count(0) > 2 or tabCheck.count(1) > 2):
      return False
  return True

def resolveTakuzu(Takuzu):
  if(checkValidity(Takuzu)):
    print("Takuzu valide")
    return Takuzu
  for i in range(len(Takuzu)):
    for j in range (len(Takuzu)):
      if(Takuzu[i][j] != 2):

