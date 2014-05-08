
from random import *

def ini():
    global A, V, NB0
    A = [[], [0]]
    NB0 = 1
    V = 1

def ajout(l):
    global A, V, NB0
    
    i = 1
    while l > 0:
        l -= A[i].count(0)
        i += 1
    i -= 1
    l += A[i].count(0)
    j = 0
    while l > 0:
        if A[i][j] == 0:
            l -= 1
        j += 1
    j -= 1
    V += 1
    A[i] = A[i][:j] + [0, V] + A[i][j:]
    A.append([0])
#    print A
    NB0 += 2

def constr(n):
    global A, NB0, V
      
    ajout(1)
    for l in range(3,n+1):
        ajout(randint(1,NB0))
        
def rm0():
    global A
    for i in range(1,len(A)):
        A[i] = [elt for elt in A[i] if elt >0]

def print_file(f):
    global A

    fic = open(f, 'w')
    fic.write('digraph { node [shape=point]; edge [arrowhead=none];\n')

    for i in range(1,len(A)):
        for j in A[i]:
            fic.write(str(i) + ' -> ' + str(j) + ';\n')
    
    fic.write('}')
    fic.close()


A = [[], [0]]
NB0 = 1
V = 1

taille_arbre = 200
ini()
constr(taille_arbre)
rm0()
print_file('arbre.dot')
