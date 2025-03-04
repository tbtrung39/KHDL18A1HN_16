n = int(input("Nhập vào số nguyên dương n: "))  
while n <= 0:  
    n = int(input("Vui lòng nhập số nguyên dương n: "))   
tong = 0  
for i in range(1, n + 1):  
    tong += 1 / i  
# In kết quả  
print("Tổng nghịch đảo từ 1 đến", n, "là:", tong)  