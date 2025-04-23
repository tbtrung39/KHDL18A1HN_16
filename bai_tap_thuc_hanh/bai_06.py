import random
n = int(input("Nhập số n:"))
A = list(range(1,n+1))
result = []
while A :
    vi_tri = random.randint(0, len(A)-1)
    gia_tri = A.pop(vi_tri)
    result.append(gia_tri)
print("Hoán vị ngẫu nhiên của dãy từ 1 đến", n, "là:",result)
