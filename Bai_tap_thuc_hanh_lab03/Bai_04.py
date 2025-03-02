import math
n = int(input("Nhập n:"))
so_nguyen_to_nho_n = 0
for i in range(n - 1,0,-1):
    flag = True
    if i <= 1:
        flag = False
    elif i == 2 or i == 3:
        flag = True
    elif i % 2 == 0:
        flag = False
    else:
        for j in range(3,int(math.sqrt(i))+1,2):
            if i % j == 0:
                flag = False
                break
    if flag :
        so_nguyen_to_nho_n = i
        print(f"Số nguyên tố < {n} là: {so_nguyen_to_nho_n}")

        


