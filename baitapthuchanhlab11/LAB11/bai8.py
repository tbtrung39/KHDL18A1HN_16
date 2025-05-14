import os

def nhap_nhan_vien():
    ma_nv = input("Nhập Mã NV: ")
    ten_nv = input("Nhập Tên NV: ")
    chuc_vu = input("Nhập Chức vụ (TP/PP/NV): ").upper()
    he_so_luong = float(input("Nhập Hệ số lương: "))
    return {"ma_nv": ma_nv, "ten_nv": ten_nv, "chuc_vu": chuc_vu, "he_so_luong": he_so_luong}
def tinh_luong(nhan_vien):
    nhan_vien["luong"] = nhan_vien["he_so_luong"] * 1490000
    return nhan_vien
def tinh_phu_cap(nhan_vien):
    chuc_vu = nhan_vien["chuc_vu"]
    if chuc_vu == "TP":
        nhan_vien["phu_cap"] = 1000000
    elif chuc_vu == "PP":
        nhan_vien["phu_cap"] = 700000
    elif chuc_vu == "NV":
        nhan_vien["phu_cap"] = 300000
    else:
        nhan_vien["phu_cap"] = 0
    return nhan_vien

def tinh_thuc_linh(nhan_vien):
    nhan_vien["thuc_linh"] = nhan_vien["luong"] + nhan_vien["phu_cap"]
    return nhan_vien

def luu_danh_sach(danh_sach_nv, ten_tep):
    thu_muc_files = "files"
    os.makedirs(thu_muc_files, exist_ok=True)
    duong_dan_tep = os.path.join(thu_muc_files, ten_tep)
    with open(duong_dan_tep, 'w', encoding='utf-8') as f:
        f.write("Mã NV,Tên NV,Chức vụ,Hệ số lương,Lương,Phụ cấp,Thực lĩnh\n")
        for nv in danh_sach_nv:
            f.write(f"{nv['ma_nv']},{nv['ten_nv']},{nv['chuc_vu']},{nv['he_so_luong']},{nv.get('luong', 0)},{nv.get('phu_cap', 0)},{nv.get('thuc_linh', 0)}\n")
    print(f"Đã lưu danh sách nhân viên vào '{duong_dan_tep}'")

def hien_thi_danh_sach(danh_sach_nv):
    print("-" * 70)
    print(f"{'Mã NV':<10}{'Tên NV':<20}{'Chức vụ':<10}{'HS Lương':<10}{'Lương':<10}{'Phụ cấp':<10}{'Thực lĩnh':<10}")
    print("-" * 70)
    for nv in danh_sach_nv:
        print(f"{nv['ma_nv']:<10}{nv['ten_nv']:<20}{nv['chuc_vu']:<10}{nv['he_so_luong']:<10.2f}{nv.get('luong', 0):<10,.0f}{nv.get('phu_cap', 0):<10,.0f}{nv.get('thuc_linh', 0):<10,.0f}")
    print("-" * 70)

def sap_xep_theo_thuc_linh(danh_sach_nv):
    return sorted(danh_sach_nv, key=lambda nv: nv.get('thuc_linh', 0), reverse=True)

def main():
    danh_sach_nhan_vien = []

    while True:
        print("\n--- MENU QUẢN LÝ NHÂN VIÊN ---")
        print("1. Nhập danh sách nhân viên")
        print("2. Hiển thị danh sách nhân viên")
        print("3. Sắp xếp theo Thực lĩnh (giảm dần) và hiển thị")
        print("4. Lưu danh sách vào file")
        print("0. Thoát")

        lua_chon = input("Nhập lựa chọn: ")

        if lua_chon == '1':
            so_luong = int(input("Nhập số lượng nhân viên: "))
            for _ in range(so_luong):
                nv = nhap_nhan_vien()
                nv = tinh_luong(nv)
                nv = tinh_phu_cap(nv)
                nv = tinh_thuc_linh(nv)
                danh_sach_nhan_vien.append(nv)
        elif lua_chon == '2':
            if danh_sach_nhan_vien:
                hien_thi_danh_sach(danh_sach_nhan_vien)
            else:
                print("Danh sách nhân viên trống.")
        elif lua_chon == '3':
            if danh_sach_nhan_vien:
                danh_sach_da_sap_xep = sap_xep_theo_thuc_linh(danh_sach_nhan_vien)
                hien_thi_danh_sach(danh_sach_da_sap_xep)
            else:
                print("Danh sách nhân viên trống.")
        elif lua_chon == '4':
            if danh_sach_nhan_vien:
                luu_danh_sach(danh_sach_nhan_vien, "ds_nhanvien.csv")
            else:
                print("Danh sách nhân viên trống.")
        elif lua_chon == '0':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()