n = int(input("Nhập số nguyên dương n: "))
# Tam giác sao rỗng dạng (a)
print("Tam giác sao rỗng dạng (a):")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i: 
            print("*", end=" ")
        else:
            print(" ", end=" ")  
    print()
# Tam giác sao rỗng dạng (b)
print("Tam giác sao rỗng dạng (b):")
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == 1 or j == n or j == i:  
            print("*", end=" ")
        else:
            print(" ", end=" ")  
    n -= 1
    print()
# Tam giác sao rỗng dạng (c)
print("Tam giác sao rỗng dạng (c):")
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == 1 or j == n or j == i:  
            print("*", end=" ")
        else:
            print(" ", end=" ")  
    print()