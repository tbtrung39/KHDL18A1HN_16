
import math
n = int(input("Nhập n: "))
for num in range(2, n + 1):
    a = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            a = False
            break
    if a:
        print(num, end=" ")
print()
