import giai_phuong_trinh

def main():
    while True:
        try:
            print("\n--- Giải phương trình ---")
            choice = input("Chọn loại phương trình (1: bậc nhất, 2: bậc hai, thoat): ").lower()

            if choice == 'thoat':
                break
            elif choice == '1':
                a = float(input("Nhập hệ số a: "))
                b = float(input("Nhập hệ số b: "))
                result = giai_phuong_trinh.giai_phuong_trinh_bac_nhat(a, b)
                print(result)
            elif choice == '2':
                a = float(input("Nhập hệ số a: "))
                b = float(input("Nhập hệ số b: "))
                c = float(input("Nhập hệ số c: "))
                result = giai_phuong_trinh.giai_phuong_trinh_bac_hai(a, b, c)
                print(result)
            else:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

        except ValueError:
            print("Lỗi: Vui lòng nhập số hợp lệ cho các hệ số.")
        except Exception as e:
            print(f"Đã xảy ra lỗi không mong muốn: {e}")

if __name__ == "__main__":
    main()