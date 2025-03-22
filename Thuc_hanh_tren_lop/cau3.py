#c1
n = int(input("Nhập số tự nhiên n: "))
binary = ""
if n == 0:
    binary = "0"
while n > 0:
    binary = str(n % 2) + binary  
    n = n // 2 
print("Số nhị phân là:", binary)

##c2
n = int(input("Nhập số tự nhiên n: "))
binary = bin(n)[2:]  
print("Số nhị phân là:", binary)
