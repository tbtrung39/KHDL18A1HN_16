a = input("Nhập dãy số nguyên, cách nhau bởi khoảng trắng: ").split()
for i in range(len(a)):
    a[i] = int(a[i])

n = len(a)
dem = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] == a[j]:
            dem += 1
            print("Cặp:", (i, j))

print("Tổng số cặp:", dem)
