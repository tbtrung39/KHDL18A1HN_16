import xu_ly_day_so

def main():
    print("--- Chương trình xử lý dãy số ---")
    day_so = xu_ly_day_so.sinh_day_so_ngau_nhien()
    if isinstance(day_so, str):
        print(day_so)
        return

    print("Dãy số ngẫu nhiên:", day_so)

    nguyen_to_chia_het_7 = xu_ly_day_so.liet_ke_nguyen_to_chia_het_cho_7(day_so)
    if nguyen_to_chia_het_7:
        print("Các số nguyên tố chia hết cho 7 trong dãy:", nguyen_to_chia_het_7)
    else:
        print("Không có số nguyên tố nào chia hết cho 7 trong dãy.")

    tong_so_le = xu_ly_day_so.tinh_tong_so_le(day_so)
    print("Tổng các số lẻ trong dãy:", tong_so_le)

    so_chinh_phuong = xu_ly_day_so.kiem_tra_so_chinh_phuong(day_so)
    if so_chinh_phuong:
        print("Các số chính phương trong dãy:", so_chinh_phuong)
    else:
        print("Không có số chính phương trong dãy.")

if __name__ == "__main__":
    main()