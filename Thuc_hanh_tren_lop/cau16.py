a = list(map(int, input("Nhập dãy số nguyên (cách nhau bởi dấu cách): ").split()))
n = len(a)
pairs = []

for i in range(n):
    for j in range(i, n):
        if a[i] + 1 == a[j]:
            pairs.append((i, j))
print("Các cặp chỉ số (i, j) thỏa mãn điều kiện a[i] + 1 = a[j]:")
for pair in pairs:
    print(pair)