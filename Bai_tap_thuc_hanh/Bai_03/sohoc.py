import math
def Ucln(a,b):
    if b == 0:
        return a
    return Ucln(b, a % b)

def Bcnn(a,b):
    return (a * b)/Ucln(a,b)
def SumDivisor(n):
    lst = []
    for i in range(1,n):
        if n % i == 0:
            lst.append(i)
    return sum(lst), lst