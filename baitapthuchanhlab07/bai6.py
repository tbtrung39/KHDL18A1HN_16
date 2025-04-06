n_str = input("Nhập một số tự nhiên n: ")
if n_str.isdigit():
    n = int(n_str)
    if n <= 0:
        print("n phải là số tự nhiên dương.")
    else:
        so_nguyen_to_dau_tien = []
        num = 2
        while len(so_nguyen_to_dau_tien) < n:
            la_nt = True
            if num < 2:
                la_nt = False
            else:
                for i in range(2, int(num**0.5) + 1):
                    if num % i == 0:
                        la_nt = False
                        break
            if la_nt:
                so_nguyen_to_dau_tien.append(num)
            num += 1
        print(f"{n} số nguyên tố đầu tiên là:", so_nguyen_to_dau_tien)
else:
    print("Vui lòng nhập một số tự nhiên hợp lệ.")