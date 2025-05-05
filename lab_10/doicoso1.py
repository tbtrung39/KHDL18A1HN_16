#Bước 1(Bài 5 ):

def nhap_so_nguyen():
    while True:
        try:
            so_nguyen = int(input("Vui lòng nhập một số nguyên: "))
            return so_nguyen
        except ValueError:
            print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")

def in_so_nguyen(so_nguyen):
    print("Số nguyên bạn vừa nhập là:", so_nguyen)

def chuyen_doi_nhi_phan(so_nguyen):
    so_nhi_phan = bin(so_nguyen)
    print("Số nhị phân:", so_nhi_phan)

def chuyen_doi_bat_phan(so_nguyen):
    so_bat_phan = oct(so_nguyen)
    print("Số bát phân:", so_bat_phan)

def chuyen_doi_thap_luc_phan(so_nguyen):
    so_thap_luc_phan = hex(so_nguyen)
    print("Số thập lục phân:", so_thap_luc_phan)