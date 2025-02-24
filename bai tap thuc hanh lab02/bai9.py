KW = int(input("nhap so dien tieu thu:"))
tien_dien = float(0)
if 0 <=KW <=100:
    tien_dien = 2000* KW
    print("so tien dien la %0.2f"%tien_dien)
elif 101<= KW <= 200:
    tien_dien = 2500 *KW
    print("so tien dien la %0.2f"%tien_dien)
elif 201<= KW <= 300:
    tien_dien= 3000 *KW
    print("so tien dien la %0.2f"%tien_dien)
elif KW>300:
    tien_dien = 5000 *KW
    print("so tien dien la %0.2f"%tien_dien)
else:
    print("so KW ko hop le, vui long nhap lail")