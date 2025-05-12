# main.py

from hinhhoc import chu_vi_hinh_vuong, dien_tich_hinh_vuong
from hinhhoc import chu_vi_tam_giac, dien_tich_tam_giac

def main():
    print("Hình vuông:")
    a = 5
    print(f" - Cạnh: {a}")
    print(f" - Chu vi: {chu_vi_hinh_vuong(a)}")
    print(f" - Diện tích: {dien_tich_hinh_vuong(a)}")

    print("\nTam giác:")
    a, b, c = 3, 4, 5
    h = 4
    print(f" - Các cạnh: {a}, {b}, {c}")
    print(f" - Chu vi: {chu_vi_tam_giac(a, b, c)}")
    print(f" - Diện tích (đáy {a}, chiều cao {h}): {dien_tich_tam_giac(a, h)}")

if __name__ == "__main__":
    main()