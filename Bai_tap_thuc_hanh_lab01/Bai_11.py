n1 = int(input("Nhập số lần tung xúc xắc: "))
# Xác suất khi tung ra số 6 là:
A = 1/6
# Xác suất khi tung không ra số 6 là:
B = 1 - A
# Tung 3 xúc xắc không có lần nào ra 6 trong n lần tung là:
C = (B**3)**n1
# Vậy xác suất khi tung n lần có ít nhất 1 lần cả 3 đều ra 6 là:
D = 1 - C
print(f"Xác suất khi tung n lần có ít nhất 1 lần cả 3 đều ra 6 là:{D} ")
