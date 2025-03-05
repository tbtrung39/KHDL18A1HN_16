# Yêu cầu nhập lại nếu n <= 0, chỉ dùng for
for _ in range(1000):  # Lặp nhiều lần để đảm bảo nhập đúng
    n = int(input("Nhập số nguyên dương n: "))
    if n > 0:
        break  # Khi nhập đúng thì thoát vòng lặp

# Lưu số gốc để in kết quả
so_goc = n

# Khởi tạo chuỗi kết quả
ket_qua = ""

# Phân tích thừa số nguyên tố
for i in range(2, n + 1):  # Duyệt từ 2 đến n
    while n % i == 0:  # Kiểm tra nếu i là ước của n
        ket_qua += str(i) + " x "
        n //= i  # Chia n cho i

# Loại bỏ dấu " × " cuối cùng
ket_qua = ket_qua[:-3]  

# In kết quả
print("Phân tích số gốc thành thừa số nguyên tố:", so_goc, ket_qua)