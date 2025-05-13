def nhap_so():
    try:
        n = int(input("Nhập một số nguyên: "))
        return n
    except ValueError:
        print("Giá trị không hợp lệ. Vui lòng nhập số nguyên.")
        return nhap_so()

def in_so(n):
    print(f"Số vừa nhập: {n}")

def doi_nhi_phan(n):
    print(f"Hệ nhị phân: {bin(n)[2:]}")

def doi_bat_phan(n):
    print(f"Hệ bát phân: {oct(n)[2:]}")

def doi_thap_luc_phan(n):
    print(f"Hệ thập lục phân: {hex(n)[2:].upper()}")