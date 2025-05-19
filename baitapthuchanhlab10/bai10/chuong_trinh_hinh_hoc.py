import my_square
import my_Triange

def main():
    print("--- Chương trình sử dụng package hinhhoc ---")
    print("\n--- Tam giác ---")
    while True:
        try:
            a = float(input("Nhập cạnh a của tam giác: "))
            b = float(input("Nhập cạnh b của tam giác: "))
            c = float(input("Nhập cạnh c của tam giác: "))

            if my_Triange.is_TamGiac(a, b, c):
                print("Đây là một tam giác.")
                print(f"Chu vi: {my_Triange.ChuViTamGiac(a, b, c)}")
                print(f"Diện tích: {my_Triange.DienTichTamGiac(a, b, c)}")
            else:
                print("Đây không phải là một tam giác.")
            break
        except ValueError:
            print("Lỗi: Vui lòng nhập số hợp lệ cho các cạnh.")
    print("\n--- Hình vuông ---")
    while True:
        try:
            canh = float(input("Nhập cạnh của hình vuông: "))
            chu_vi = my_square.ChuViHinhVuong(canh)
            dien_tich = my_square.DienTichHinhVuong(canh)
            if isinstance(chu_vi, str):
                print(chu_vi)
                print(dien_tich)
            else:
                print(f"Chu vi: {chu_vi}")
                print(f"Diện tích: {dien_tich}")
            break
        except ValueError:
            print("Lỗi: Vui lòng nhập số hợp lệ cho cạnh.")

if __name__ == "__main__":
    main()