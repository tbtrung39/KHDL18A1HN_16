from doicoso import doicoso1, doicoso2

def test_doicoso1():
    print("\n--- Chuyển đổi số nguyên ---")
    n = doicoso1.nhap_so_nguyen()
    print("Hệ nhị phân:", doicoso1.doi_nhi_phan(n))
    print("Hệ bát phân:", doicoso1.doi_bat_phan(n))
    print("Hệ thập lục phân:", doicoso1.doi_thap_luc_phan(n))

def test_doicoso2():
    print("\n--- Xử lý chuỗi cơ số ---")
    s = input("Nhập chuỗi cơ số bất kỳ: ")
    s_loc = doicoso2.loc_ky_tu_hop_le(s)
    coso = doicoso2.co_so_nao(s_loc)
    if coso == 2:
        print("Chuỗi thuộc hệ nhị phân. Giá trị thập phân:", doicoso2.nhi_phan_sang_thap_phan(s_loc))
    elif coso == 8:
        print("Chuỗi thuộc hệ bát phân. Giá trị thập phân:", doicoso2.bat_phan_sang_thap_phan(s_loc))
    elif coso == 16:
        print("Chuỗi thuộc hệ thập lục phân. Giá trị thập phân:", doicoso2.thap_luc_phan_sang_thap_phan(s_loc))
    else:
        print("Không xác định được hệ cơ số.")

def main():
    print("=== SỬ DỤNG PACKAGE doicoso ===")
    test_doicoso1()
    test_doicoso2()

if __name__ == "__main__":
    main()