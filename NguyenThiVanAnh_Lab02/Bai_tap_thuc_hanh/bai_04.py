n=int(input("Nhap vao mot so nguyen: "))
if n<0:
    n=-n
if n>=100:
    chu_so_hang_tram=(n//100)%10
else:
    chu_so_hang_tram=0
print("Chu so hang tram la: ",chu_so_hang_tram)
