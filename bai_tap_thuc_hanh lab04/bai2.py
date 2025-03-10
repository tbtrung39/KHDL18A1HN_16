######caua
n = 1
s = 0
sign = 1
max_terms = int(input('nhap so phan tu'))
while n <= max_terms:
    s += sign / n
    sign *= -1
    n +=1
print(f"tong sau{max_terms} phan tu la: {s}")
####caub
s = 0
i = 2
n = int(input("nhap n"))
while i <= n:
    s += 1/(i*(i+1))
    i += 1
print(f"tong s den n = {n} la: {s}")
####cauc
import math
s = 0
i = 2
n = int(input("nhap n: "))
while i <= n:
    s += 1/math.sqrt(i)
    i += 1
    print(f"tong s den n = {n} la; {s}")
    