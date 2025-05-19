def ChuViHinhVuong(a):
    if not isinstance(a, (int, float)):
        return "Lỗi: Cạnh phải là một số."
    if a <= 0:
        return "Lỗi: Cạnh phải là số dương."
    return 4 * a

def DienTichHinhVuong(a):
    if not isinstance(a, (int, float)):
        return "Lỗi: Cạnh phải là một số."
    if a <= 0:
        return "Lỗi: Cạnh phải là số dương."
    return a * a

if __name__ == "__main__":
    print("Đây là module my_square. Vui lòng chạy file chương trình chính để sử dụng.")