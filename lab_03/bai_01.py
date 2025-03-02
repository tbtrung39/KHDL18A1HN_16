n=int(input("Nhap n: "))
tong=1
tich=1
for i in range(n+1):
    tich=(2*(i+1))/(2*i+3)
    tong+=tich
print("Ket qua= %0.3f"%tong)