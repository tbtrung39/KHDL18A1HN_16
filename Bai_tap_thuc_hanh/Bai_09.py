n = int(input("Nhập vào số nguyên dương n: "))    
while n <= 0:  
    n = int(input("Vui lòng nhập số nguyên dương n: "))   
S4 = 0  
S5 = 0  
S6 = 0  
for i in range(1, n + 1):  
    S4 += i ** 2  
    S5 += (2 * i - 1) ** 3  
    S6 += (4 * i) ** 4  
print("S4 =", S4)  
print("S5 =", S5)  
print("S6 =", S6)  