import random
n_str = input("Nhập số lượng phần tử ngẫu nhiên cho tập hợp A (là số nguyên): ")
if n_str.isdigit():
    n = int(n_str)
    if n <= 0:
        print("Vui lòng nhập số nguyên dương.")
    else:
        tap_hop_a_ngau_nhien = set()
        for _ in range(n):
            so_thuc_ngau_nhien = random.random() * 100
            tap_hop_a_ngau_nhien.add(so_thuc_ngau_nhien)
        print("Tập hợp A ngẫu nhiên:", tap_hop_a_ngau_nhien)
        if tap_hop_a_ngau_nhien:
            min_val = min(tap_hop_a_ngau_nhien)
            max_val = max(tap_hop_a_ngau_nhien)
            tong_val = sum(tap_hop_a_ngau_nhien)
            print("Phần tử nhỏ nhất của tập hợp A:", min_val)
            print("Phần tử lớn nhất của tập hợp A:", max_val)
            print("Tổng các phần tử của tập hợp A:", tong_val)
        else:
            print("Tập hợp A rỗng.")
else:
    print("Lỗi: Vui lòng nhập một số nguyên cho n.")