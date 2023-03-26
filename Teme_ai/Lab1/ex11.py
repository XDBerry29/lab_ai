"""
Considerându-se o mat cu n x m elemente binare (0 sau 1), să se înlocuiască cu 1 toate aparițiile elementelor egale cu 0 care sunt complet înconjurate de 1.

De ex. mata \ 
[[1,1,1,1,0,0,1,1,0,1],
[1,0,0,1,1,0,1,1,1,1],
[1,0,0,1,1,1,1,1,1,1],
[1,1,1,1,0,0,1,1,0,1],
[1,0,0,1,1,0,1,1,0,0],
[1,1,0,1,1,0,0,1,0,1],
[1,1,1,0,1,0,1,0,0,1],
[1,1,1,0,1,1,1,1,1,1]]
*devine *
[[1,1,1,1,0,0,1,1,0,1],
[1,1,1,1,1,0,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,0,1],
[1,1,1,1,1,1,1,1,0,0],
[1,1,1,1,1,1,1,1,0,1],
[1,1,1,0,1,1,1,0,0,1],
[1,1,1,0,1,1,1,1,1,1]]
"""

from queue import Queue

# Definim vectorii deplasare pentru cele 4 directii
deplasare_x=[-1 , 0 , 1 , 0]
deplasare_y=[0, -1 , 0 , 1]

def verif(cur,mat,aux):
    if cur[0]>=0 and cur[1]>=0 and cur[0]< len(mat) and cur[1]< len(mat[1]) and mat[cur[0]][cur[1]] == 0 and aux[cur[0]][cur[1]] == 1:
        return True
    
    return False


def parcurgere(mat, aux, x ,y):
    aux[x][y] = 0 # Marcam pozitia (x,y) in matricea 'aux' ca fiind vizitata
    cur = (x,y)

    queue = Queue()
    queue.put(cur)

    #parcurgem si marcam peninsulele
    while (not queue.empty()):
        (x,y) = queue.get()

        # Verificam fiecare pozitie adiacenta
        for i in range(4):
            cur = (x+deplasare_x[i],y+deplasare_y[i])
            if verif(cur,mat,aux):
                queue.put(cur)
                aux[cur[0]][cur[1]] = 0

    return aux
            



def inlocuire(mat):
    n = len(mat)
    m = len(mat[0])

    # initializare mat auxiliara
    aux = [[1 for j in range(m)] for i in range(n)]

    for i in range(m):
        if(mat[0][i]==0 and aux[0][i] != 0):
           aux=parcurgere(mat,aux,0,i)

    for i in range(m):
        if mat[n-1][i]==0 and aux[n-1][i] != 0:
           aux=parcurgere(mat,aux,n-1,i)

    for i in range(n):
        if mat[i][0]==0 and aux[i][0] != 0 :
           aux=parcurgere(mat,aux,i,0)

    for i in range(n):
        if mat[i][m-1]==0 and aux[i][m-1] != 0 :
           aux=parcurgere(mat,aux,i,m-1)


    

    return aux

def test_inlocuire():
    mat = [[1,1,1,1,0,0,1,1,0,1],
          [1,0,0,1,1,0,1,1,1,1],
          [1,0,0,1,1,1,1,1,1,1],
          [1,1,1,1,0,0,1,1,0,1],
          [1,0,0,1,1,0,1,1,0,0],
          [1,1,0,1,1,0,0,1,0,1],
          [1,1,1,0,1,0,1,0,0,1],
          [1,1,1,0,1,1,1,1,1,1]]

    expected = [[1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
                [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                [1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
                [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]]

    assert inlocuire(mat) == expected
    print("All tests passed!")



test_inlocuire()