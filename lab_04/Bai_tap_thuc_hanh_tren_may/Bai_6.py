# Nhập số nguyên từ bàn phím
print("Nhập số nguyên dương:")
so = input()  # Đọc số dưới dạng chuỗi để dễ xử lý từng chữ số

# Khởi tạo biến
i = 0
ket_qua = ""

# Duyệt từng chữ số và chuyển thành chữ
while i < len(so):
    chu_so = so[i]  # Lấy từng chữ số dạng chuỗi
    
    if chu_so == "0":
        ket_qua += "không "
    elif chu_so == "1":
        ket_qua += "một "
    elif chu_so == "2":
        ket_qua += "hai "
    elif chu_so == "3":
        ket_qua += "ba "
    elif chu_so == "4":
        ket_qua += "bốn "
    elif chu_so == "5":
        ket_qua += "năm "
    elif chu_so == "6":
        ket_qua += "sáu "
    elif chu_so == "7":
        ket_qua += "bảy "
    elif chu_so == "8":
        ket_qua += "tám "
    elif chu_so == "9":
        ket_qua += "chín "
    
    i += 1  # Tăng biến đếm

# In kết quả
print("Số dưới dạng chữ:", ket_qua.strip())