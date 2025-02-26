n = int(input("Nhập n: "))
for num in range(2, n):
    tong = 0
    for i in range(1, num):
        if num % i == 0:
            tong += i
    if tong == num:
        print(f"Số hoàn hảo: {num}")
        