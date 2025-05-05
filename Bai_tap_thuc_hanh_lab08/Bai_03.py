import math
def ktr_so_nguyen_to(dem):
    if dem <= 1:
        return False
    elif dem == 2 or dem == 3:
        return True
    else:
        for i in range(2,int(math.sqrt(dem)+1)):
            if dem % i == 0:
                return False
        return True

def so_nguyen_to_nho_hon_n(n):
    dem = 0
    while dem <= n:
        if ktr_so_nguyen_to(dem):
            print(dem,end=" ")
        dem += 1
n = int(input("Nhập  n số nguyên tố: "))
print(so_nguyen_to_nho_hon_n(n))
