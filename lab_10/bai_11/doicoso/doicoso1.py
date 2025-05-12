def nhap_so():
    n = int(input("Nhap mot so nguyen: "))
    print(f"So vua nhap la: {n}")
    return n

def doi_nhi_phan(n):
    print("Dang nhi phan:", bin(n))

def doi_bat_phan(n):
    print("Dang bat phan:", oct(n))

def doi_thap_luc_phan(n):
    print("Dang thap luc phan:", hex(n))