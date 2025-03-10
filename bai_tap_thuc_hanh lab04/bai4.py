tu_so = float(input("nhap tu so: "))
mau_so = float(input("nhap mau so: "))
while mau_so==0:
    print("mau so khong the bang 0. vui long nhap lai mau so.")
    mau_so = float(input("nhap mau so: "))
    print(f"phan so ban nhap la: {tu_so}/{mau_so}")