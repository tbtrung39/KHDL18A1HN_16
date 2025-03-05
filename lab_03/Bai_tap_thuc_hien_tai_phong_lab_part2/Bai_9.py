# Yêu cầu nhập lại nếu n <= 0, nhưng chỉ dùng for
for _ in range(1000):  # Duyệt với số lần lặp lớn để đảm bảo nhập đúng
    n = int(input("Nhập số nguyên dương n: "))
    if n > 0:
        break  # Khi nhập đúng thì thoát vòng lặp

# Khởi tạo các tổng
S4 = 0
S5 = 0
S6 = 0

# Tính S4 = 1^2 + 2^2 + 3^2 + ... + n^2
for i in range(1, n + 1):
    S4 += i ** 2

# Tính S5 = 1^3 + 3^3 + 5^3 + ... + (2n+1)^3
for i in range(1, 2 * n + 2, 2):  # Duyệt số lẻ từ 1 đến (2n+1)
    S5 += i ** 3

# Tính S6 = 2^4 + 4^4 + 6^4 + ... + (2n)^4
for i in range(2, 2 * n + 1, 2):  # Duyệt số chẵn từ 2 đến 2n
    S6 += i ** 4

# In kết quả
print("Tổng S4 =", S4)
print("Tổng S5 =", S5)
print("Tổng S6 =", S6)