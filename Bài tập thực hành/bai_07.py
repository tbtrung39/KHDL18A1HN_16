a,b,c = map(float,input('Nhập giá trị a,b,c của phương trình bậc 2 :').split())
x_dinh= -b/(2*a)
y_dinh= (4*a*c-b**2)/4*a
print(f'Đỉnh của phương trình bậc 2 đó là: ({x_dinh:.2f},{y_dinh:.2f})')
