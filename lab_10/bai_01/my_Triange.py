def is_TamGiac(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False

def ChuviTamGiac(a,b,c):
    if is_TamGiac(a, b, c):
        return a+b+c
    else:
        return None

import math
def S_TamGiac(a,b,c):
    if is_TamGiac(a, b, c):
        p=(a+b+c)/2
        s=math.sqrt(p*(p-a)*(p-b)*(p-c))
        return s
    else:
        return None


