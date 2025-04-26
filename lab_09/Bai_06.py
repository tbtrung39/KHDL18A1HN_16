import random

def hoan_vi_ngau_nhien(a, result=None):
    if result is None:
        result = []
    if not a:
        return result
    index = random.randint(0, len(a) - 1)
    result.append(a[index])
    a.pop(index)
    return hoan_vi_ngau_nhien(a, result)

n = int(input("Nhập số nguyên n: "))
A = list(range(1, n + 1))
ket_qua = hoan_vi_ngau_nhien(A)
print("Hoán vị ngẫu nhiên:", ket_qua)