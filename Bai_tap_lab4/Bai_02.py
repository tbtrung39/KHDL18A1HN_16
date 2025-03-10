#a
n = 100   
S = 0  
for i in range(1, n + 1):  
    S += (-1) ** (i + 1) / i  
print(f"Tổng a với {n} phần tử là: {S}")  
#b
n = 100  
S = 0  
for i in range(2, n + 2):  
    S += 1 / (i * (i + 1))  
print(f"Tổng b với {n} phần tử là: {S}")  
#c
import math  
n = 100   
S = 0  
for i in range(2, n + 2):  
    S += 1 / math.sqrt(i)  
print(f"Tổng c với {n} phần tử là: {S}") 