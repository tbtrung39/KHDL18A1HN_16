# Nhập danh sách số tự nhiên từ bàn phím, cách nhau bởi dấu cách
numbers = list(map(int, input("Nhập các số tự nhiên: ").split()))

# Tạo tập hợp từ danh sách để loại bỏ số trùng lặp
A = set(numbers)

# Hiển thị kết quả
print("Danh sách Numbers:", numbers)
print("Tập hợp A:", A)