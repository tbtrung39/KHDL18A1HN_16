n = int(input("Nhap so hang: "))
for i in range(n):
    for j in range(n - i - 1):   
        print(" ", end="")
    for j in range(2 * i + 1):  
        if j == 0 or j == 2 * i or i == n - 1:
            print("*", end="")   
        else:
            print(" ", end="")   
    print()

for i in range(n):
    for j in range(n - i - 1): 
        print(" ", end="")
    for j in range(i + 1):   
        if j == 0 or j == i or i == n - 1:
            print("* ", end="")   
        else:
            print("  ", end="") 
    print()

for i in range(n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()
