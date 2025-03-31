import random
A = [random.randint(1, 99999) for _ in range(1000)]
A_sorted = sorted(A)
print("10 phần tử đầu sau khi sắp xếp (dùng sorted):", A_sorted[:10], "...")
A_copy = A.copy()
n = len(A_copy)
for i in range(n):
    for j in range(0, n-i-1):
        if A_copy[j] > A_copy[j+1]:
            A_copy[j], A_copy[j+1] = A_copy[j+1], A_copy[j]  
print("10 phần tử đầu sau khi sắp xếp (không dùng sorted):", A_copy[:10], "...")