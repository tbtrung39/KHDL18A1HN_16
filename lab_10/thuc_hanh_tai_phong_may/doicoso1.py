def nhap_so_nguyen():
    so = int(input("Nhập một số nguyên: "))
    return so

def doi_sang_nhi_phan(n):
    return bin(n)[2:]  # Loại bỏ '0b'

def doi_sang_bat_phan(n):
    return oct(n)[2:]  # Loại bỏ '0o'

def doi_sang_thap_luc_phan(n):
    return hex(n)[2:].upper()  # Loại bỏ '0x' và viết hoa