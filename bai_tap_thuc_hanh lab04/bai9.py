N = int(input('Nhập N: '))
N = abs(N)
tong = 0
while N > 0:
    tong += N % 10
    N //= 10
print('Tổng các chữ số là:', tong)