import doicoso1

def main():
    print("--- Chương trình chuyển đổi cơ số ---")
    so_da_nhap = doicoso1.nhap_so_nguyen()
    print(f"Số đã nhập: {so_da_nhap}")

    nhi_phan = doicoso1.sang_nhi_phan(so_da_nhap)
    print(f"Hệ nhị phân: {nhi_phan}")

    bat_phan = doicoso1.sang_bat_phan(so_da_nhap)
    print(f"Hệ bát phân: {bat_phan}")

    thap_luc_phan = doicoso1.sang_thap_luc_phan(so_da_nhap)
    print(f"Hệ thập lục phân: {thap_luc_phan}")

if __name__ == "__main__":
    main()