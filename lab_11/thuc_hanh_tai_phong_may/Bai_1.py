# Mở tập tin để đọc
taptin = open("thuc_hanh_tai_phong_may\dayso.dat", "r")

# Tạo biến tổng để cộng các số lẻ
tong_le = 0

# Đọc từng dòng trong tập tin
dong = taptin.readline()
while dong != "":
    # Tách các số trên dòng thành danh sách các chuỗi
    cac_so = dong.split()

    # Duyệt qua từng chuỗi số
    for so in cac_so:
        x = int(so)           # Ép kiểu sang số nguyên
        if x % 2 == 1:        # Nếu là số lẻ
            tong_le = tong_le + x

    # Đọc dòng tiếp theo
    dong = taptin.readline()

# Đóng tập tin
taptin.close()

# In kết quả
print("Tổng các số lẻ là:", tong_le)