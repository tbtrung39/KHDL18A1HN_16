
a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]: 
            a[i], a[j] = a[j], a[i]
print("Danh sách sau khi sắp xếp tăng dần:", a)
