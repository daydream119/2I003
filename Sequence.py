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

a = "ATCGGCTGCATTTCGA"
print(tailleMaxRec(a, 2, 12))
print(tailleMaxRec(a, 0, len(a)-1)) #Too slow
#print(tailleMaxRec("AT", 0, 1))
