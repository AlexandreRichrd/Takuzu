from winreg import REG_QWORD


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