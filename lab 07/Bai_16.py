a = [1, 2, 3, 2, 4]
n = len(a)
pairs = []
for i in range(n-1):
    for j in range(i+1, n):
        if a[i] + 1 == a[j]:
            pairs.append((i, j))
print(pairs)