import random
def hoan_vi_ngau_nhien(n):
    A = [i + 1 for i in range(n)]
    result = []
    while A:
        chon = random.choice(A)
        result.append(chon)
        A.remove(chon)
    return result
n = int(input("Nhập số phần tử: "))
print("Một hoán vị ngẫu nhiên của dãy là:")
print(hoan_vi_ngau_nhien(n))