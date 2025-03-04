hang = int(input("Nhập số hàng tam giác: "))   
for i in range(1, hang + 1):  
    print("* " * i)  
print() 
for i in range(1, hang + 1):  
    print(" " * (hang - i) + "* " * i)  
print()
for i in range(1, hang + 1):  
    print(" " * (hang - i) + "* " * (2 * i - 1))  