# 13. suma elementelor este egal cu 5
# 14. oricare doua elemente consecutive au cel putin 2 cifre distincte comune
def meniu():
    print("1.Citirea unei liste de numere intregi.")
    print("2.Gasirea secventelor de lungime maxima care au suma elementelor egala cu 5.")
    print("3.Gasirea secventelor de lungime maxima in care oricare doua elemente consecutive au cel putin 2 cifre distincte comune.")
    print("4.Gasirea secventelor de lungime maxima care sunt formate numai din numere negative.")
    print("5. Iesire din aplicatie.")

def citirelista():
    l = []
    n = int(input("Dati lungimea sirului: "))
    for i in range(n):
        x = int(input())
        l.append(x)
    return l

def suma5(l):
    '''
    se afla lungimea maxima a secventelor de lungime maxima care au suma elementelor egala cu 5
    :param l: lista
    :return: lungimea maxima
    '''
    lmax = 0
    nrsecv = 0
    for i in range(0, len(l)):
        s = 0
        lg = 0
        j = i
        while s < 5 and j < len(l):
            s = s + l[j]
            lg = lg + 1
            j = j + 1
        if s == 5:
            if lg == lmax:
                nrsecv = nrsecv + 1
            elif lg > lmax:
                nrsecv = 1
                lmax = lg
    return lmax


def AfisSuma5(l):
    lg=suma5(l)
    if lg == 0:
        print("Nu exista secvente de lungime maxima care au suma elementelor egala cu 5")
    else:
        print("Lungimea maxima a secventelor care au suma elementelor egala cu 5 este: "+str(lg))

def testSuma5():
    l = [3,1,1,1,3]
    assert suma5(l) == 3
    l = [5,2,6]
    assert suma5(l) == 1
    l=[12,11,10]
    assert suma5(l) == 0

def testCifredistincte():
    assert (Cifredistincte(21, 12) == True)
    assert (Cifredistincte(231, 12) == True)
    assert (Cifredistincte(3, 12) == False)

def Cifredistincte(x, y):
    '''
    determina daca doua numere consecutive au cel putin doua cifre distincte comune
    :param x: primul nr care este verificat
    :param y: al doilea nr care este verificat
    :return: True daca x si y au cel putin doua cifre distincte comune,False in caz contrar
    '''
    fr1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fr2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    nrC = 0
    if x < 0:
        x = x*(-1)
    if y < 0:
        y = y*(-1)
    while x != 0:
        fr1[x % 10] += 1
        x = x // 10
    while y != 0:
        fr2[y % 10] += 1
        y = y // 10
    for d in range(0, 10):
        if fr1[d] == 1 and fr2[d] == 1:
            nrC = nrC + 1
    if nrC >= 2:
        return True
    else:
        return False


def Douacifredistinctecomune(l):
    '''
    se afla lungimea maxima a secventelor de lungime maxima in care oricare doua elemente consecutive au cel putin 2 cifre distincte comune.
    :param l: lista
    :return: lungimea maxima
    '''
    lmax = 0
    lg = 1
    nrsecv = 0
    for i in range(0, len(l) - 1):
        x = l[i]
        y = l[i + 1]
        if Cifredistincte(x, y) == True:
            lg = lg + 1
        else:
            if lg == lmax:
                nrsecv = nrsecv + 1
                lg = 1
            elif lg > lmax and lg != 1:
                nrsecv = 1
                lmax = lg
                lg = 1
    if lg == lmax:
        nrsecv = nrsecv + 1
    elif lg > lmax:
        nrsecv = 1
        lmax = lg
    return lmax

def Afiscifredsitincte(l):
    lg=Douacifredistinctecomune(l)
    if lg == 1:
        print("Nu exista secvente de lungime maxima in care oricare doua elemente consecutive au cel putin 2 cifre distincte comune.")
    else:
        print("Lungimea maxima asecventelor in care oricare doua elemente consecutive au cel putin 2 cifre distincte comune este: "+str(lg))

def testCifredistincte():
    l =[12,21,3]
    assert (Douacifredistinctecomune(l) == 2 )
    l = [51,52,12]
    assert (Douacifredistinctecomune(l) == 1 )
    l = [45,54,3,9435,854]
    assert (Douacifredistinctecomune(l) == 2 )

def Nrnegative(l):
    '''
    se afla lungimea maxima a secventelor de lungime maxima care sunt formate numai din numere negative
    :param l: lista
    :return: lungimea maxima
    '''
    lmax = 0
    nrsecv = 0
    lg = 0
    for i in range(0, len(l)):
        if l[i] < 0:
            lg = lg + 1
        else:
            if lg == lmax and lmax != 0:
                nrsecv += 1
                lg = 0
            elif lg > lmax:
                lmax = lg
                lg = 0
                nrsecv = 1
            lg = 0
    if lg == lmax and lmax != 0:
        nrsecv += 1
        lg = 0
    elif lg > lmax:
        lmax = lg
        lg = 0
        nrsecv = 1
    return lmax

def AfisNrNegative(l):
    lg=Nrnegative(l)
    if lg == 0:
        print ("Nu exista secvente de lungime maxima care sunt formate numai din numere negative.")
    else:
        print("Lungimea maxima a secventelor care sunt formate numai din numere negative este: "+str(lg))

def testNrNegative():
    l = [-1,-1,-1]
    assert (Nrnegative(l) == 3 )
    l = [23,-3,9]
    assert (Nrnegative(l) == 1 )
    l = [2,39,10]
    assert (Nrnegative(l) == 0 )

def testall():
    testCifredistincte()
    testSuma5()
    testNrNegative()

def main():
    # l=[0,0,0,0,0,0,0,0,0,0]
    l = []
    while True:
        meniu()
        tasta = input("Dati optiunea: ")
        if tasta == "1":
            l = citirelista()
        elif tasta == "2":
            AfisSuma5(l)
        elif tasta == "3":
            Afiscifredsitincte(l)
        elif tasta == "4":
            AfisNrNegative(l)
        elif tasta == "5":
            break
        else:
            print("Optiune invalida. Reincercati.")

testall()

main()
