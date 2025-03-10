n=int(input("Nhap so nguyen n: "))
tong=0
while n>0:
    tong+=n%10
    n//=10
print(f"Tong cac chu so cua {n} la: {tong}")