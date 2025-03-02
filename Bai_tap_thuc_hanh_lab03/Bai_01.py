n = int(input("Nhap n: "))
S = 1
X = 1
for i in range(1,n+1):
    X*= 2*(i+1)/(2*n+3)
    S+=X
print(S)