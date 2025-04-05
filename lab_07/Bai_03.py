
n = int(input("Nhap so phan tu cua tap hop A: "))
A = []
print("Nhap cac phan tu cua tap hop A:")
for i in range(n):
    num = float(input("Phan tu thu " + str(i + 1) + ": "))
    A.append(num)
min_val = min(A)
max_val = max(A)
sum_val = sum(A)
print("Ket qua:")
print("Tap hop A: " + str(A))
print("Phan tu nho nhat: " + str(min_val))
print("Phan tu lon nhat: " + str(max_val))
print("Tong cac phan tu: " + str(sum_val))