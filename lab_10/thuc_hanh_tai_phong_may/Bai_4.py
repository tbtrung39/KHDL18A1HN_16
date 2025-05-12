# bai_4.py

import giai_pt

def main():
    print("Giải phương trình bậc nhất: ax + b = 0")
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    print(giai_pt.giai_pt_bac_nhat(a, b))

    print("\nGiải phương trình bậc hai: ax^2 + bx + c = 0")
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    c = float(input("Nhập c: "))
    print(giai_pt.giai_pt_bac_hai(a, b, c))

if __name__ == "__main__":
    main()