import my_square

def main():
    while True:
        try:
            canh = float(input("Nhập độ dài cạnh của hình vuông: "))

            chu_vi = my_square.ChuViHinhVuong(canh)
            dien_tich = my_square.DienTichHinhVuong(canh)

            if isinstance(chu_vi, str):  
                print(chu_vi)
                print(dien_tich) 
            else:
                print(f"Chu vi hình vuông là: {chu_vi}")
                print(f"Diện tích hình vuông là: {dien_tich}")

            tiep_tuc = input("Bạn có muốn tính cho hình vuông khác không?: ")
            if tiep_tuc.lower() != 'y':
                break

        except ValueError:
            print("Lỗi: Vui lòng nhập số hợp lệ cho độ dài cạnh.")
        except Exception as e:
            print(f"Đã xảy ra lỗi không mong muốn: {e}")

if __name__ == "__main__":
    main()