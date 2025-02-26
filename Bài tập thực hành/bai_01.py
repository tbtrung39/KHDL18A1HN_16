n = int(input("Nhập n:"))
S=1
for i in range(1,n+1):
    phan_tu_dau=(2/3)
    for j in range(1,i):
        phan_tu_dau *= ( 2*j+2)/(2*j+3)
    S += phan_tu_dau
print(f"Giá trị của biểu thức là :{S:.3f}")