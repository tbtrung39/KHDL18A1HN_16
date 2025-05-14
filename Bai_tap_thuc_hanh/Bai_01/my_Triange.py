import math
def is_TamGiac(a,b,c):
    if a + b > c and a + c > b and b + c > a :
        return True
    return False

def ChucviTamGiac(a,b,c):
    return (a + b+ c)/3

def S_TamGiac(a,b,c):
    p = (a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))


