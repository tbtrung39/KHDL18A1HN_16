#a
n = int(input ("Nhap gia tri n: "))
S = 0
i = 1
while i <= n:
    if i % 2 ==0:
        S -= 1 / i
    else:
        S += 1/i
    i += 1
print("Tong S=", S)


#b
n = int(input ("Nhap gia tri n: "))
S = 0
i = 2
while i <= n:
    S += 1/ (i*(i+1))
    i += 1
print("Tong S=", S)



#c
import math
n = int(input ("Nhap gia tri n: "))
S = 0
i = 2
while i <= n:
    S += 1/ math.sqrt(i)
    i += 1
print("Tong S=", S)


