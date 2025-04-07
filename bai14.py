# Bài 14: Tạo từ điển nhị phân từ 1 đến 10

n = 10
d = {}

for i in range(1, n+1):
    so = i
    nhi_phan = ""
    while so > 0:
        bit = so % 2
        nhi_phan = str(bit) + nhi_phan
        so = so // 2
    d[i] = nhi_phan

print("Từ điển nhị phân:")
for k in d:
    print(k, ":", d[k])
