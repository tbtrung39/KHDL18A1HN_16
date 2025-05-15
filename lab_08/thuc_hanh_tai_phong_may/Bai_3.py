def la_so_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def in_cac_so_nguyen_to_nho_hon(n):
    print(f"Các số nguyên tố nhỏ hơn {n} là:")
    for i in range(2, n):
        if la_so_nguyen_to(i):
            print(i, end=' ')

# Chương trình chính
n = int(input("Nhập một số nguyên dương n: "))
in_cac_so_nguyen_to_nho_hon(n)