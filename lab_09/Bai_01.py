def lon_nhat(a,b):
    if a > b:
        return a
    else:
        return b

def so_max(x,y,z):
    return lon_nhat(x , lon_nhat(y,z))

a = float(input("Nhập số thứ nhất:"))
b = float(input("Nhập số thứ hai:"))
c = float(input("Nhập số thứ ba:"))

KQ = so_max(a,b,c)
print("số lớn nhất là :",KQ)