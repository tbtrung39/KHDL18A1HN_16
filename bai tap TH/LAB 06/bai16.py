X = int(input("Nhập X: "))  
Y = int(input("Nhập Y: "))  
mang_2chieu = [[i * j for j in range(Y)] for i in range(X)]  
print(mang_2chieu)