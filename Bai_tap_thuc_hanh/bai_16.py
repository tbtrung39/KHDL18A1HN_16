a = [1, 2, 3, 2, 4]  
n = len(a)
for i in range(n):
    for j in range(i + 1, n):
        if a[i] + 1 == a[j]:
            print("(", i + 1, ",", j + 1, ")")