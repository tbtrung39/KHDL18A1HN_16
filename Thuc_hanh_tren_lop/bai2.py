################a
n = int(input("Nhập số lượng phần tử n: "))
s = 0
i = 1
while i <= n:
    if i % 2 != 0:  
        s += 1 / i
    else: 
        s -= 1 / i
    i += 1
print(f"Tổng S = {s}")


##########b
n = int(input("Nhập số phần tử n: "))  
s = 0
i = 2  
while i <= n + 1:  
    s += 1 / (i * (i + 1))  
    i += 1  
print(f"Tổng S = {s}")


################c
n = int(input("Nhập số phần tử n: "))
s, i = 0, 2
while i <= n + 1:
    s += 1 / (i ** 0.5)  
    i += 1
print(s)
