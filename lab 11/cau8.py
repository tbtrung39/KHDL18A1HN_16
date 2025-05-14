
import os
import csv
def tao_thu_muc_va_file():
    os.makedirs('LAB11/files', exist_ok=True)
    open('LAB11/qlynhanvien.py', 'a').close()
    open('LAB11/libs/xu_ly_thong_tin_nhanvien.py', 'a').close()
    open('LAB11/files/ds_nhanvien.csv', 'a').close()
def main():
    ds_nhan_vien = []
    while True:
        print("\n===== QUẢN LÝ NHÂN VIÊN =====")
        print("1. Nhập thông tin nhân viên")
        print("2. Tính lương và phụ cấp")
        print("3. Hiển thị danh sách nhân viên")
        print("4. Sắp xếp theo thực lĩnh giảm dần")
        print("5. Lưu dữ liệu vào file CSV")
        print("0. Thoát")
        
        chon = input("Chọn chức năng: ")
        
        if chon == '1':
            n = int(input("Nhập số lượng nhân viên: "))
            for i in range(n):
                print(f"\nNhập thông tin nhân viên thứ {i+1}:")
                ma_nv = input("Mã NV: ")
                ten_nv = input("Tên NV: ")
                chuc_vu = input("Chức vụ (TP/PP/NV): ").upper()
                he_so_luong = float(input("Hệ số lương: "))
                
                nhan_vien = {
                    'MaNV': ma_nv,
                    'TenNV': ten_nv,
                    'ChucVu': chuc_vu,
                    'HeSoLuong': he_so_luong,
                    'Luong': 0,
                    'PhuCap': 0,
                    'ThucLinh': 0
                }
                ds_nhan_vien.append(nhan_vien)
        elif chon == '2':
            for nv in ds_nhan_vien:
                nv['Luong'] = nv['HeSoLuong'] * 1490000
                if nv['ChucVu'] == 'TP':
                    nv['PhuCap'] = 1000000
                elif nv['ChucVu'] == 'PP':
                    nv['PhuCap'] = 700000
                else:
                    nv['PhuCap'] = 300000
                nv['ThucLinh'] = nv['Luong'] + nv['PhuCap']
            print("Đã tính toán xong lương và phụ cấp!")
        elif chon == '3':
            print("\nDANH SÁCH NHÂN VIÊN")
            print("| {:<10} | {:<20} | {:<10} | {:<12} | {:<15} | {:<15} | {:<15} |".format(
                "Mã NV", "Tên NV", "Chức vụ", "Hệ số lương", "Lương", "Phụ cấp", "Thực lĩnh"))
            for nv in ds_nhan_vien:
                print("| {:<10} | {:<20} | {:<10} | {:<12} | {:<15,.0f} | {:<15,.0f} | {:<15,.0f} |".format(
                    nv['MaNV'], nv['TenNV'], nv['ChucVu'], nv['HeSoLuong'], 
                    nv['Luong'], nv['PhuCap'], nv['ThucLinh']))
        elif chon == '4':
            ds_sap_xep = sorted(ds_nhan_vien, key=lambda x: x['ThucLinh'], reverse=True)
            print("\nDANH SÁCH SAU KHI SẮP XẾP")
            print("| {:<10} | {:<20} | {:<15} |".format("Mã NV", "Tên NV", "Thực lĩnh"))
            for nv in ds_sap_xep:
                print("| {:<10} | {:<20} | {:<15,.0f} |".format(
                    nv['MaNV'], nv['TenNV'], nv['ThucLinh']))
        elif chon == '5':
            with open('LAB11/files/ds_nhanvien.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=['MaNV', 'TenNV', 'ChucVu', 'HeSoLuong', 'Luong', 'PhuCap', 'ThucLinh'])
                writer.writeheader()
                writer.writerows(ds_nhan_vien)
            print("Đã lưu dữ liệu vào file ds_nhanvien.csv")
        
        elif chon == '0':
            break
        else:
            print("Lựa chọn không hợp lệ!")
if __name__ == "__main__":
    tao_thu_muc_va_file()
    main()
