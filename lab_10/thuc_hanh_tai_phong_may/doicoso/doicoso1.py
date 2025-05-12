def nhap_so_nguyen():
    n = int(input("Nhập một số nguyên: "))
    print("Số vừa nhập là:", n)
    return n

def doi_nhi_phan(n):
    return bin(n)

def doi_bat_phan(n):
    return oct(n)

def doi_thap_luc_phan(n):
    return hex(n)