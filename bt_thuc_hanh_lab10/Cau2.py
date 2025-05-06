# Cau 2
def ucln_tu_mau(x,y):
    while y != 0:
        x,y = y, x % y
    return x

def rut_gon(x,y):
    tu = x / ucln_tu_mau(x,y)
    mau = y / ucln_tu_mau(x,y)
    return f"{int(tu)}/{int(mau)}"
x = int(input("Nhập tử: "))
y = int(input("Nhập mẫu: "))
print(rut_gon(x,y))
        
    