def nhap_so():
    n = int(input("Nhập một số nguyên: "))
    print(f"Số vừa nhập là: {n}")
    return n

def doi_nhi_phan(n):
    print(f"Hệ nhị phân: {bin(n)[2:]}")

def doi_bat_phan(n):
    print(f"Hệ bát phân: {oct(n)[2:]}")

def doi_thap_luc_phan(n):
    print(f"Hệ thập lục phân: {hex(n)[2:].upper()}")
