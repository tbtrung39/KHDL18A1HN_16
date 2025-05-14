def hoan_vi(danh_sach, vi_tri):
    if vi_tri == len(danh_sach):
        print(danh_sach)
        return
    for i in range(vi_tri, len(danh_sach)):
        danh_sach[vi_tri], danh_sach[i] = danh_sach[i], danh_sach[vi_tri]
        hoan_vi(danh_sach, vi_tri + 1)
        danh_sach[vi_tri], danh_sach[i] = danh_sach[i], danh_sach[vi_tri]
n = int(input("Nhập số tự nhiên n: "))
day = list(range(1, n + 1))
print(f"Tất cả các hoán vị của dãy từ 1 đến {n} là:")
hoan_vi(day, 0)