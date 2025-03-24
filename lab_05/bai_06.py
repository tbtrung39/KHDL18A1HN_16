str=input("Nhap chuoi: ")
s_hex="0123456789ABCDEFabcdef"
s=""
for c in str:
    if c in s_hex:
        s+=c
if s=="":
    print("Khong co ki tu hop le de chuyen doi.")
else:
    n=int(s,16)
    print("Chuoi hop le thu duoc:",s)
    print("Gia tri thap phan tuong ung:",n)