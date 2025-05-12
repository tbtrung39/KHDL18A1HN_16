import doicoso1

def main():
    print("=== CHUYỂN ĐỔI CƠ SỐ ===")
    n = doicoso1.nhap_so_nguyen()
    
    print(f"Số vừa nhập: {n}")
    print(f"Hệ nhị phân: {doicoso1.doi_sang_nhi_phan(n)}")
    print(f"Hệ bát phân: {doicoso1.doi_sang_bat_phan(n)}")
    print(f"Hệ thập lục phân: {doicoso1.doi_sang_thap_luc_phan(n)}")

if __name__ == "__main__":
    main()