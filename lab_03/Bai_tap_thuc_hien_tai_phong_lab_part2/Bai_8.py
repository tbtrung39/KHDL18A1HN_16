# Yêu cầu nhập lại nếu n <= 0, nhưng chỉ dùng for
for _ in range(1000):  # Duyệt với số lần lặp lớn để đảm bảo nhập đúng
    n = int(input("Nhập số nguyên dương n: "))
    if n > 0:
        break  # Khi nhập đúng thì thoát vòng lặp

# Khởi tạo các tổng
S1 = 0
S2 = 0
S3 = 0

# Tính S1 = 1 + 2 + 3 + ... + n
for i in range(1, n + 1):
    S1 += i

# Tính S2 = 1 + 3 + 5 + ... + (2n+1)
for i in range(1, 2 * n + 2, 2):  # Duyệt số lẻ từ 1 đến (2n+1)
    S2 += i

# Tính S3 = 2 + 4 + 6 + ... + 2n
for i in range(2, 2 * n + 1, 2):  # Duyệt số chẵn từ 2 đến 2n
    S3 += i

# In kết quả
print("Tổng S1 =", S1)
print("Tổng S2 =", S2)
print("Tổng S3 =", S3)