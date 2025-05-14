import csv
import os

def nhap_danh_sach_sv():
    danh_sach = []
    n = int(input("Nhập số lượng sinh viên: "))
    for _ in range(n):
        ma_sv = input("Mã SV: ")
        ho_ten = input("Họ tên: ")
        diem_tb = float(input("Điểm TB: "))
        diem_rl = float(input("Điểm RL: "))
        diem_tl = (diem_tb + diem_rl) / 2
        sinh_vien = [ma_sv, ho_ten, diem_tb, diem_rl, diem_tl]
        danh_sach.append(sinh_vien)
    return danh_sach

def in_danh_sach_sv(danh_sach):
    print("{:<10} {:<20} {:<10} {:<10} {:<10}".format("Mã SV", "Họ Tên", "Điểm TB", "Điểm RL", "Điểm TL"))
    for sv in danh_sach:
        print("{:<10} {:<20} {:<10.2f} {:<10.2f} {:<10.2f}".format(*sv))

def luu_vao_file(danh_sach, filename="C:\\Users\\Admin\\OneDrive\\Thực hành lập trình cơ bản KHDL\\KHDL18A1HN_16\\Bai_tap_thuc_hanh\\Bai_10\\files"):
    os.makedirs("files", exist_ok=True)
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Mã SV", "Họ Tên", "Điểm TB", "Điểm RL", "Điểm TL"])
        writer.writerows(danh_sach)

def sap_xep_theo_diem_rl(danh_sach):
    return sorted(danh_sach, key=lambda sv: sv[3])  # sv[3] là điểm RL

def tim_sv_diem_tl_cao_nhat(danh_sach):
    max_tl = max(danh_sach, key=lambda sv: sv[4])  # sv[4] là điểm TL
    return max_tl
