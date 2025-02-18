a, b, c= map(float,input("Nhap vao cac gia tri a,b,c cua phuong trinh bac hai: ").split())
x_dinh=-b/(2*a)
y_dinh=(4*a*c - b**2)/(4*a)
print(f"Toa do dinh cua phuong trinh tren la: ({x_dinh:.2f};{y_dinh:.2f})")
