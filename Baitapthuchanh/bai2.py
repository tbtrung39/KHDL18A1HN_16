n = int(input("Nhập n: "))
for i in range(2, n):
    tong_uoc = 1
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            tong_uoc = tong_uoc + j + i // j
    if tong_uoc == i:
        print(i, end=" ")