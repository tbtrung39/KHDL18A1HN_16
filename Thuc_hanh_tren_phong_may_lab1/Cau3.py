# 3

def tinh_khoi_tru(r, h):
    pi = 3.14  # Giá trị của π theo đề bài
    dien_tich_xung_quanh = 2 * pi * r * h
    dien_tich_toan_phan = 2 * pi * r * (r + h)
    the_tich = pi * r**2 * h
    
    # In trực tiếp trong hàm
    print(f"Diện tích xung quanh: {round(dien_tich_xung_quanh, 2)}")
    print(f"Diện tích toàn phần: {round(dien_tich_toan_phan, 2)}")
    print(f"Thể tích khối trụ: {round(the_tich, 2)}")

# Nhập dữ liệu từ bàn phím
r = float(input("Nhập bán kính khối trụ: "))
h = float(input("Nhập chiều cao khối trụ: "))

# Gọi hàm mà không cần return
tinh_khoi_tru(r, h)