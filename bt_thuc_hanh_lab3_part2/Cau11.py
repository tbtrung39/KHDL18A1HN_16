# Câu 11
n = int(input("Nhập số hàng: "))
# (hình a)
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")  
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2 or i == n:
            print("*", end="") 
        else:
            print(" ", end="")  
    print()  
print()  
# (hình b)
for i in range(1, n + 2):  
    for j in range(n - i + 1):
        print(" ", end="")  
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2 or i == n + 1:
            print("*", end="") 
        else:
            print(" ", end="") 
    print()  
# (hình c)
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")  
    for j in range(2 * i - 1):
        print("*", end="")  
    print()  
print()  
