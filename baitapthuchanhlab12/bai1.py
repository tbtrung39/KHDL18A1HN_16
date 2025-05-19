import math

def nhap_canh(loai_canh):
    while True:
        try:
            canh_str = input(f"Nhập độ dài cạnh {loai_canh}: ")
            canh = float(canh_str)
            if canh <= 0:
                print("Lỗi: Độ dài cạnh phải là số dương.")
            else:
                return canh
        except ValueError:
            print("Lỗi: Vui lòng nhập một số hợp lệ.")

def la_tam_giac(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

def tinh_dien_tich(a, b, c):
    s = (a + b + c) / 2
    dien_tich = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return dien_tich

def main():
    danh_sach_dien_tich = []
    while True:
        print("\n--- Nhập thông tin tam giác ---")
        try:
            a = nhap_canh("a")
            b = nhap_canh("b")
            c = nhap_canh("c")

            if la_tam_giac(a, b, c):
                dien_tich = tinh_dien_tich(a, b, c)
                danh_sach_dien_tich.append(dien_tich)
                print(f"Diện tích tam giác là: {dien_tich:.2f}")
            else:
                print("Lỗi: Ba cạnh này không tạo thành một tam giác hợp lệ.")

        except Exception as e:
            print(f"Đã xảy ra lỗi không mong muốn: {e}")

        tiep_tuc = input("Bạn có muốn nhập thêm tam giác khác không?: ")
        if tiep_tuc.lower() != 'y':
            break

    print("\n--- Danh sách diện tích các tam giác hợp lệ đã nhập")
    if danh_sach_dien_tich:
        for i, dien_tich in enumerate(danh_sach_dien_tich):
            print(f"Tam giác thứ {i+1}: {dien_tich:.2f}")
    else:
        print("Chưa có tam giác hợp lệ nào được nhập.")

if __name__ == "__main__":
    main()