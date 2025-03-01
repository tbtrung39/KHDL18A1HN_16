# Chuỗi chứa các ký tự chữ cái và số tương ứng
chu_cai = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
gia_tri = [10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
           21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 
           32, 34, 35, 36, 37, 38]

# Nhập chuỗi container chuẩn (10 ký tự)
container = input("Nhập mã container (10 ký tự): ")

# Kiểm tra độ dài hợp lệ
while len(container) != 10:
    print("Mã container phải có đúng 10 ký tự!")
    container = input("Nhập lại mã container: ")

# Chuyển ký tự đầu tiên thành giá trị số
so_tong = 0
for i in range(10):
    ky_tu = container[i]

    # Nếu là chữ cái, lấy giá trị từ danh sách
    if 'A' <= ky_tu <= 'Z':
        for j in range(26):
            if chu_cai[j] == ky_tu:
                gia_tri_so = gia_tri[j]
                break
    else:
        gia_tri_so = int(ky_tu)  # Nếu là số, giữ nguyên giá trị

    # Nhân với 2^n theo yêu cầu bài toán
    so_tong += gia_tri_so * (2 ** i)

# Tính số kiểm tra bằng cách chia tổng cho 11
so_kiem_tra = so_tong % 11

# In kết quả
print("Số kiểm tra của container là:", so_kiem_tra)


bang_giatri = {
    'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19,
    'J': 20, 'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29,
    'S': 30, 'T': 31, 'U': 32, 'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38
}
ma_container = input("Nhập mã container (10 ký tự): ")
tong = 0
for i in range(len(ma_container)):
    ky_tu = ma_container[i]

    if ky_tu.isdigit():
        giatri = int(ky_tu)  
    else:
        giatri = bang_giatri[ky_tu]  
    tong += giatri * (2 ** i)
so_kiem_tra = tong % 11
if so_kiem_tra == 10:
    so_kiem_tra = 0
print("Số kiểm tra là:", so_kiem_tra)