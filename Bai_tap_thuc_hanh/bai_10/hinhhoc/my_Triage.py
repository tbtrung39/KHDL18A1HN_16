import math

def ChuviTamGiac(a, b, c):
    return a + b + c

def DienTichTamGiac(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))  
