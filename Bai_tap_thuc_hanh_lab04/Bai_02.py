# ý a:
n = int(input("Nhập n: "))
S = 0
i = 1
while i <= n:
    if i % 2 == 0:
        S -= 1/i
    else:
        S += 1/i
    i += 1
print(S)
# ý b:
n1 = int(input("Nhập n: "))
S1 = 0
j = 1
while j <= n1:
    S1 += 1/(j*(j + 1))
    j += 1
print(S1)
# ý c: 
import math
n2 = int(input("Nhập n2: "))
S3 = 0
k = 2
while k <= n2:
    S3 += 1/(math.sqrt(k))
    k += 1
print(S3)


    