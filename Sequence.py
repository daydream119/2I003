from random import randint

def match(a, i, j):
    if(a[i] == "A" and a[j] == "T"):
        return 1
    if(a[i] == "T" and a[j] == "A"):
        return 1
    if(a[i] == "C" and a[j] == "G"):
        return 1
    if(a[i] == "G" and a[j] == "C"):
        return 1
    else:
        return 0

def findMaxInRange(a, i, j):
    l = []
    for k in range(i+1, j+1): #i allant de i+1 à j
        l.append(tailleMaxRec(a, i, k-1) + tailleMaxRec(a, k, j))
    return max(l)

def tailleMaxRec(a, i, j):
    if(a == "" or i >= j):
        return 0
    else:
        return max(tailleMaxRec(a, i+1, j-1) + match(a, i, j), findMaxInRange(a, i, j))

def tailleMaxIter(a):
    n = len(a)
    #initialiser une matrice n*n partout de 0
    E = [[0 for l in range(n)] for j in range(n)]
    #p allant de 1 à n-1
    for p in range(1, n):
        #i allant de 0 à n-p-1
        for i in range(n-p):
            j = p+i
            #k allant de i à j
            l = []
            for k in range(i, j+1):
                l.append(E[i][k-1] + E[k][j])
            x = max(l)
            E[i][j] = max(E[i+1][j-1]+match(a, i, j), x)
    return E[0][n-1]



def SeqAleatoire(n):
    seq = ""
    alph = ["A", "G", "C", "T"]
    for c in range(n):
        i = randint(0, 3)
        seq += alph[i]
    return seq

def testTime(n):
    import time
    a = SeqAleatoire(n)
    start1 = time.time()
    tailleMaxIter(a)
    end1 = time.time()
    t1 = end1 - start1
    print("Le temps d'exécution de manière itérative sur la séquence de taille "+ str(n) + " est " + str(t1) + "s")
    start2 = time.time()
    tailleMaxRec(a, 0, len(a)-1)
    end2 = time.time()
    t2 = end2 - start2
    print("Le temps d'exécution de manière récursive sur la séquence de taille " + str(n) + " est " + str(t2) + "s")

if __name__ == '__main__':
    testTime(15) #  presque 0 seconde vs 20 secondes
