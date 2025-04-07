
n = int(input("Nhap so phan tu cua tap hop A: "))
A = []
print("Nhap cac phan tu cua tap hop A:")
for i in range(1, n + 1):
    num = float(input(f"Phan tu thu {i}: "))
    A.append(num)
min_val = min(A)
max_val = max(A)
sum_val = sum(A)
print("\n--- Ket qua ---")
print("Tap hop A:", A)
print("Phan tu nho nhat:", min_val)
print("Phan tu lon nhat:", max_val)
print("Tong cac phan tu:", sum_val)
