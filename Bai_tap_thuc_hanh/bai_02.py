n = int(input("Nhập n:"))
while n <= 0:
    n = int(input("Nhập lại n:"))
S1=0
i=1
while i <=n:
    S1+=1/i
    i+=1
print("Tông S1 =",S1)

n = int(input("Nhập n:"))
while n <= 0:
    n = int(input("Nhập lại n:"))
S2=0
i=2
while i <=n:
    S2+=1/(i*(i+1))
    i+=1
print("Tông S2 =",S2)

import math
n = int(input("Nhập n:"))
while n <= 0:
    n = int(input("Nhập lại n:"))
S3=0
i=22
while i <=n:
    S3+=1/ math.sqrt(i)
    i+=1
print("Tông S3 =",S3)