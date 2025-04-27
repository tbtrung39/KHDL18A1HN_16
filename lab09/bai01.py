def lon_nhat(a,b):
    if a > b:
        return a
    else:
        return b

def tim_lon_nhat_3_so(x,y,z):
    return lon_nhat(x , lon_nhat(y,z))

a = float(input("Nhập số thứ nhất:"))
b = float(input("Nhập số thứ hai:"))
c = float(input("Nhập số thứ ba:"))

ket_qua = tim_lon_nhat_3_so(a,b,c)
print("số lớn nhất là :",ket_qua)