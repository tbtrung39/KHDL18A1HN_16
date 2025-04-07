nhap_vao = input("Nhập các số tự nhiên, cách nhau bởi dấu cách: ")
numbers = [int(x) for x in nhap_vao.split()]
A = set(numbers)
print("Danh sách ban đầu:", numbers)
print("Tập hợp (không trùng lặp):", A)