X = int(input("Nhập số hàng (X): "))
Y = int(input("Nhập số cột (Y): "))
array = []
for i in range(X):  
    row = []  
    for j in range(Y): 
        row.append(i * j)  
    array.append(row)  
print("Mảng 2 chiều:")
for row in array:
    print(row)