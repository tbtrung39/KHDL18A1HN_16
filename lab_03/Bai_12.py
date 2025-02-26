
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