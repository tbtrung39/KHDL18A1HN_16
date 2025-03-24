# Bước 1: Nhập chuỗi từ bàn phím
str_hex = input("Nhập chuỗi: ")

# Bước 2: Khai báo chuỗi chứa các ký tự hợp lệ của hệ HEX
hex_chars = "0123456789ABCDEFabcdef"

# Bước 3: Duyệt chuỗi, loại bỏ các ký tự không hợp lệ
chuoi_hop_le = ""

for c in str_hex:  # Duyệt từng ký tự trong chuỗi nhập vào
    if c in hex_chars:
        chuoi_hop_le += c  # Nếu là ký tự HEX, thêm vào chuỗi hợp lệ

# Bước 4: Kiểm tra và chuyển đổi nếu chuỗi hợp lệ không rỗng
if chuoi_hop_le:
    so_thap_phan = 0
    l = len(chuoi_hop_le)

    # Chuyển đổi thủ công từ hệ HEX sang thập phân
    for i in range(l):
        char = chuoi_hop_le[i]
        
        # Xác định giá trị của ký tự trong hệ HEX
        if '0' <= char <= '9':
            value = ord(char) - ord('0')  # Chuyển '0'-'9' thành số 0-9
        else:
            value = ord(char.upper()) - ord('A') + 10  # Chuyển 'A'-'F' thành 10-15

        # Cộng dồn vào số thập phân theo công thức hệ 16
        so_thap_phan = so_thap_phan * 16 + value  

    print(f"Chuỗi HEX hợp lệ: {chuoi_hop_le}")
    print(f"Số thập phân tương ứng: {so_thap_phan}")
else:
    print("Không có ký tự nào hợp lệ trong hệ HEX!")

