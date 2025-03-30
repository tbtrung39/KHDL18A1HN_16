m = int(input("Nhập số hàng (m): "))
n = int(input("Nhập số cột (n): "))

ma_trận = []
tổng = 0

print("Nhập ma trận (mỗi hàng cách nhau bởi dấu phẩy):")
for i in range(m):
    hàng_nhập = input()
    hàng_số = []
    số_chuoi = ""
    for ký_tự in hàng_nhập:
        if ký_tự == ',':
            hàng_số.append(int(số_chuoi))
            tổng += int(số_chuoi)
            số_chuoi = ""
        else:
            số_chuoi += ký_tự
    hàng_số.append(int(số_chuoi))  # Thêm số cuối cùng
    tổng += int(số_chuoi)
    ma_trận.append(hàng_số)

print("Ma trận A:")
for hàng in ma_trận:
    print(hàng)

print(f"Tổng các phần tử của ma trận A: {tổng}")