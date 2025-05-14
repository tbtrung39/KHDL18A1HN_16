
def tinh_tong_so_le():
    try:
        with open('dayso.dat', 'r') as file:
            tong = 0
            for line in file:
                numbers = line.strip().split()
                for num in numbers:
                    if num.isdigit() and int(num) % 2 != 0:
                        tong += int(num)
            print(f"Tổng các số lẻ trong file là: {tong}")
    except FileNotFoundError:
        print("Không tìm thấy file dayso.dat")

tinh_tong_so_le()
