n = int(input('Nhấp số lần tung xúc xắc:'))
P1 = 1/216
P= 1 - (1-P1)**n
print(f'xác suất khi tung n lần 3 xúc sắc có ít nhất 1 lần cả 3 ra 6 là : {P:.2f}')
