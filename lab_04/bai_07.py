a,b = map(int,input("Nhap vao hai so nguyen duong a va b: ").split())
bcnn=max(a,b)
while bcnn%a!=0 or bcnn%b!=0:
    bcnn+=1
print(f"BCNN cua {a} va {b} la: {bcnn}")