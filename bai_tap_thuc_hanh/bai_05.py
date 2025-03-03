a = list(map(float, input("Nhập các phần tử của vector a, cách nhau bởi dấu cách: ").split()))
b = list(map(float, input("Nhập các phần tử của vector b, cách nhau bởi dấu cách: ").split()))
if len(a) != len(b):
 print("Hai vector phải có cùng kích thước.")
else:
 tich_vo_huong = sum([a[i] * b[i] for i in range(len(a))])
 print(f"Tích vô hướng của hai vector a và b là: {tich_vo_huong}")