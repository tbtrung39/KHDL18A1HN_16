m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))
A = []  
print("Nhập các phần tử của ma trận:")
for i in range(m):
    row = []  
    for j in range(n):
        value = int(input(f"Nhập A[{i+1}][{j+1}]: "))  
        row.append(value)  
    A.append(row)  
print("Ma trận đã nhập:")
for row in A:
    print(row)
tong = 0
for row in A:
    tong += sum(row)  
print("Tổng các phần tử của ma trận:", tong)
