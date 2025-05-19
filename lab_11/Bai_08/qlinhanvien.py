import csv

from libs.xu_li_thong_tin_nhanvien import tinh_luong, tinh_phu_cap, tinh_thuc_linh

def nhap_danh_sach_nv():
    danh_sach = []
    n = int(input("Nhập số lượng nhân viên: "))
    for _ in range(n):
        ma = input("Mã NV: ")
        ten = input("Tên NV: ")
        chuc_vu = input("Chức vụ (TP/PP/NV): ")
        he_so = float(input("Hệ số lương: "))
        
        luong = tinh_luong(he_so)
        phu_cap = tinh_phu_cap(chuc_vu)
        thuc_linh = tinh_thuc_linh(luong, phu_cap)

        nv = {
            "ma": ma,
            "ten": ten,
            "chuc_vu": chuc_vu,
            "he_so": he_so,
            "luong": luong,
            "phu_cap": phu_cap,
            "thuc_linh": thuc_linh
        }

        danh_sach.append(nv)
    return danh_sach

def in_danh_sach(danh_sach):
    print(f"{'Ma NV':<10}{'Ten NV':<20}{'Chuc Vu':<8}{'He so':<8}{'Luong':<10}{'Phu cap':<10}{'Thuc linh':<10}")
    for nv in danh_sach:
        print(f"{nv['ma']:<10}{nv['ten']:<20}{nv['chuc_vu']:<8}{nv['he_so']:<8}"
              f"{nv['luong']:<10,.0f}{nv['phu_cap']:<10,}{nv['thuc_linh']:<10,.0f}")

def ghi_file_csv(danh_sach, filename="files/ds_nhanvien.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Ma NV", "Ten NV", "Chuc Vu", "He so", "Luong", "Phu cap", "Thuc linh"])
        for nv in danh_sach:
            writer.writerow([
                nv["ma"], nv["ten"], nv["chuc_vu"],
                nv["he_so"], nv["luong"], nv["phu_cap"], nv["thuc_linh"]
            ])

def main():
    danh_sach = nhap_danh_sach_nv()
    
    print("\n--- Danh sách nhân viên ---")
    in_danh_sach(danh_sach)

    danh_sach.sort(key=lambda nv: nv["thuc_linh"], reverse=True)
    print("\n--- Danh sách sau sắp xếp theo thực lĩnh giảm dần ---")
    in_danh_sach(danh_sach)

    ghi_file_csv(danh_sach)
    print("\n Đã lưu file vào 'files/ds_nhanvien.csv'")

if __name__ == "__main__":
    main()