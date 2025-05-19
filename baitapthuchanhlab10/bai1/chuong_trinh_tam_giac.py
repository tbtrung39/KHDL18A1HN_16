import my_Triange 

def main():
    while True:
        try:
            a = float(input("Nhập độ dài cạnh a: "))
            b = float(input("Nhập độ dài cạnh b: "))
            c = float(input("Nhập độ dài cạnh c: "))

            if my_Triange.is_TamGiac(a, b, c):
                print(f"Ba cạnh {a}, {b}, {c} tạo thành một tam giác.")
                chu_vi = my_Triange.ChuViTamGiac(a, b, c)
                dien_tich = my_Triange.DienTichTamGiac(a, b, c)
                print(f"Chu vi tam giác là: {chu_vi}")
                print(f"Diện tích tam giác là: {dien_tich}")
            else:
                print(f"Ba cạnh {a}, {b}, {c} không tạo thành một tam giác.")

            tiep_tuc = input("Bạn có muốn kiểm tra bộ ba cạnh khác không?: ")
            if tiep_tuc.lower() != 'y':
                break

        except ValueError:
            print("Lỗi: Vui lòng nhập số hợp lệ cho độ dài các cạnh.")
        except Exception as e:
            print(f"Đã xảy ra lỗi không mong muốn: {e}")

if __name__ == "__main__":
    main()