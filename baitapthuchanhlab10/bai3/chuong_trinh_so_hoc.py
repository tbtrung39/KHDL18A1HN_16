import sohoc
def main():
    while True:
        try:
            print("\n--- Tính toán số học ---")
            choice = input("Chọn thao tác (ucln/bcnn/tonguoc/thoat): ").lower()

            if choice == 'thoat':
                break
            elif choice == 'ucln':
                num1 = int(input("Nhập số nguyên thứ nhất: "))
                num2 = int(input("Nhập số nguyên thứ hai: "))
                result = sohoc.UCLN(num1, num2)
                print(f"Ước chung lớn nhất của {num1} và {num2} là: {result}")
            elif choice == 'bcnn':
                num1 = int(input("Nhập số nguyên thứ nhất: "))
                num2 = int(input("Nhập số nguyên thứ hai: "))
                result = sohoc.BCNN(num1, num2)
                print(f"Bội chung nhỏ nhất của {num1} và {num2} là: {result}")
            elif choice == 'tonguoc':
                num = int(input("Nhập số nguyên dương n: "))
                result = sohoc.SumDivisor(num)
                print(f"Tổng các ước của {num} là: {result}")
                if isinstance(result, str): 
                    print(result)
            else:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

        except ValueError:
            print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")
        except Exception as e:
            print(f"Đã xảy ra lỗi không mong muốn: {e}")

if __name__ == "__main__":
    main()