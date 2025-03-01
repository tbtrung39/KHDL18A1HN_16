############11a
n = int(input("Nhập số hàng (độ rộng) của tam giác: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")  
    
    for j in range(i):
        if j == 0 or j == i - 1 or i == n: 
            print("*", end=" ")
        else:
            print(" ", end=" ") 
    print()  

##########11b
n = int(input("Nhập số hàng (độ rộng) của tam giác: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        if j == 0 or j == i - 1 or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

###################11c
n = int(input("Nhập số hàng (độ rộng) của tam giác: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        if j == 0 or j == i - 1 or i == n: 
            print("*", end=" ")
        else:
            print(" ", end=" ") 
    print()  


