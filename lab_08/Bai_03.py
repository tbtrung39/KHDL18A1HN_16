def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def in_so_nguyen_to_nho_hon_N(N):
    print(f"Các số nguyên tố nhỏ hơn {N} là:")
    for i in range(2, N):
        if la_so_nguyen_to(i):
            print(i, end=' ')

N = int(input("Nhập số nguyên dương N: "))
if N <= 2:
    print("Không có số nguyên tố nào nhỏ hơn", N)
else:
    in_so_nguyen_to_nho_hon_N
