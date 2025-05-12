import xulydayso

def main():
    print("=== XỬ LÝ DÃY SỐ NGẪU NHIÊN ===")
    day = xulydayso.sinh_day_so(50)  # Bạn có thể đổi số lượng tại đây
    print("Dãy số vừa sinh:")
    print(day)

    snt_7 = xulydayso.liet_ke_snt_chia_het_7(day)
    print("\nCác số nguyên tố chia hết cho 7:")
    print(snt_7 if snt_7 else "Không có")

    tong_le = xulydayso.tong_so_le(day)
    print(f"\nTổng các số lẻ trong dãy: {tong_le}")

    scp = xulydayso.kiem_tra_va_lay_scp(day)
    if scp:
        print("\nCác số chính phương trong dãy:")
        print(scp)
    else:
        print("\nKhông có số chính phương trong dãy.")

if __name__ == "__main__":
    main()