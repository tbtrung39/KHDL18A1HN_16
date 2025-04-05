A = [1, 2, 3, 2, 4]
n = len(A)
pairs = []
for i in range(n):
    for j in range(i + 1, n):
        if A[i] + 1 == A[j]:
            pairs.append((i + 1, j + 1))
print('Cac cap chi so(i, j): ')
for pair in pairs:
    print(pair)