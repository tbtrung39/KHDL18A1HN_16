n = int(input("Nhập N: "))
print("Dạng thừa số nguyên tố của", n, "là: ")
for i in range(2,n+1):
    if n % i ==0:
     print("x",i, end="")
     n//=i