number = int(input("Nhập vào một số nguyên dương: "))  
print("Phân tích nguyên tố của số", number, "là:")  
for i in range(2, number + 1):  
    while number % i == 0:  
        print(i, end=' ')  
        number //= i  