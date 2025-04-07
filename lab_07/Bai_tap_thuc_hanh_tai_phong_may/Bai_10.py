# Nhập hai số tự nhiên từ bàn phím
m = int(input("Nhập số m: "))
n = int(input("Nhập số n: "))

# Tạo tập hợp các chữ số trong m và n
digits_m = set(str(m))  # Chuyển m thành chuỗi và lấy tập hợp chữ số
digits_n = set(str(n))  # Chuyển n thành chuỗi và lấy tập hợp chữ số

# Tìm các chữ số chung giữa hai số
common_digits = digits_m.intersection(digits_n)

# Tính tổng các chữ số chung
sum_common_digits = sum(map(int, common_digits))  # Chuyển chữ số về số nguyên và tính tổng

# In kết quả
print("Các chữ số chung:", sorted(map(int, common_digits)))
print("Tổng các chữ số chung:", sum_common_digits)