# Khai báo biến
tu_so = 0
mau_so = 0
nhap_dung = False  # Cờ kiểm tra nhập đúng

# Nhập tử số
print("Nhập tử số:")
tu_so = int(input())

# Nhập mẫu số, kiểm tra mẫu số không được bằng 0
while not nhap_dung:
    print("Nhập mẫu số (khác 0):")
    mau_so = int(input())
    
    if mau_so != 0:
        nhap_dung = True  # Thoát vòng lặp nếu nhập đúng
    else:
        print("Mẫu số không được bằng 0, vui lòng nhập lại.")

# In phân số
print("Phân số đã nhập:", tu_so, "/", mau_so)