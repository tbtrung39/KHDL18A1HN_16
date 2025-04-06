n_str = input("Nhập một số tự nhiên n : ")
if n_str.isdigit():
    n = int(n_str)
    if n <= 1:
        print("n phải là số tự nhiên lớn hơn 1.")
    else:
        tap_hop_a = set()
        tap_hop_b = set()
        for i in range(2, n + 1):
            la_nt = True
            if i < 2:
                la_nt = False
            else:
                for j in range(2, int(i**0.5) + 1):
                    if i % j == 0:
                        la_nt = False
                        break
            if la_nt:
                if n % i == 0:
                    tap_hop_a.add(i)
                else:
                    tap_hop_b.add(i)
        print("Tập hợp A (số nguyên tố là ước của n):", tap_hop_a)
        print("Tập hợp B (số nguyên tố nhỏ hơn n và không là ước của n):", tap_hop_b)
else:
    print("Vui lòng nhập một số tự nhiên hợp lệ.")