# Nhập danh sách các số từ bàn phím (dùng map để chuyển thành danh sách số nguyên)
numbers = list(map(int, input("Nhập danh sách số, cách nhau bởi dấu cách: ").split()))

# Sử dụng assert để kiểm tra tất cả các số đều là số chẵn
assert all(x % 2 == 0 for x in numbers), "Danh sách chứa số lẻ!"

# Nếu không có lỗi, in thông báo danh sách hợp lệ
print("Danh sách hợp lệ: Tất cả các số đều là số chẵn.")