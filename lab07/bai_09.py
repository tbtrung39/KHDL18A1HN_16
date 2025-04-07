n = int(input("Nhap so tu nhien n: "))
A = set()
for i in range(1, n + 1):
    if n % i == 0:
        if i < 2:
            kt = False
        else:
            kt = True
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    kt = False
                    break
        if kt:
            A.add(i)
B = set()
for i in range(2, n):
    kt = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            kt = False
            break
    if kt and n % i != 0:
        B.add(i)
print("Tap hop A (so nguyen to la uoc cua n):", A)
print("Tap hop B (so nguyen to nho hon n, khong la uoc cua n):", B)