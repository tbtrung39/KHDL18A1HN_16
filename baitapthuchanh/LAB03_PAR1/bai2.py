N = int(input("Nhập N: "))
print("Các số hoàn hảo nhỏ hơn", N, "là:")
for i in range(2, N):
    tong = 0
    for j in range(1, i):
        if i % j == 0:
            tong += j
    if tong == i:
        print(i)