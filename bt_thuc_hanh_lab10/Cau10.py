# Cau 10
def uoc(n):
    for i in range(1,n):
        if n % i == 0:
            print(i,end=" ")
n = int(input("Nhập n: "))
print(uoc(n))