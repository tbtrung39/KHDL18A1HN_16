import math

# Biểu thức a
def tinh_a(n):
    if n == 1:
        return 1 / (1 * 2)
    else:
        return 1 / (n * (n + 1)) + tinh_a(n - 1)

# Giai thừa
def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giai_thua(n - 1)

# Biểu thức b
def tinh_b(n):
    if n == 1:
        return 1
    else:
        return 1 / giai_thua(n) + tinh_b(n - 1)

# Biểu thức c
def tinh_c(n):
    if n == 1:
        return math.sqrt(3)
    else:
        return math.sqrt(3 * n + tinh_c(n - 1))
    
# Biểu thức d
def tinh_d(n):
    if n == 1:
        return math.sqrt(1)  # Căn bậc 1 của 1
    else:
        # Căn bậc n của biểu thức bên trong
        inner_value = math.pow(n - 1 + tinh_d(n - 1), 1 / n)
        return math.pow(n + inner_value, 1 / (n + 1))  # Căn bậc n+1

# --- Chạy chương trình ---
n = int(input("Nhập số tự nhiên n: "))

print("Kết quả biểu thức a:", tinh_a(n))
print("Kết quả biểu thức b:", tinh_b(n))
print("Kết quả biểu thức c:", tinh_c(n))
print("Kết quả biểu thức c:", tinh_d(n))