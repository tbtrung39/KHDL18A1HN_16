num=int(input("Nhập sô nguyên:"))
tong= 0
while num > 0 :
    tong += num % 10
    num //= 10
print("Tổng các chữ số của số đã nhập là:",tong)