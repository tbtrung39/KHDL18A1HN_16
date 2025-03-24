n = int(input("Nhập số tự nhiên n: "))
binary_str = bin(n)[2:]  # Hàm bin() trả về chuỗi dạng '0b...', nên cắt bỏ '0b'
print("Số nhị phân:", binary_str)