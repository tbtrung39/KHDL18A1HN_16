# câu 6
import random
n = int(input("Nhập số tự nhiên n: "))
A = [i for i in range(1, n + 1)]
result = []
while A:
    x = random.choice(A)  
    result.append(x)      
    A.remove(x)           
print("Hoán vị ngẫu nhiên:", result)