import math
n = int(input("Nhập n: "))
flag = True
if n <= 1:
    flag = False
elif n == 2 or n == 3:
    flag = True
else:
    if n % 2 == 0:
        flag = False
    else:
        for i in range(3,int(math.sqrt(n))+1,2):
            if n % i == 0:
                flag = False
                break
# Tìm số nguyên < n:
so_nguyen_nho_n = 0
for j in range(n-1,0,-1):
    flag_1 = True
    if j == 2 or j == 3:
        flag = True
    else:
        if j % 2 == 0:
            flag_1 = False
        else:
            for k in range(3,int(math.sqrt(j))+1,2):
                if j % k == 0:
                    flag_1 = False
                    break
    if flag_1:
        so_nguyen_nho_n = j
        break
# Tìm số nguyên > n:
so_nguyen_lon_hon_n = 0
for h in range(n,n+10000):
    flag_2 = True
    if h == 2 or h == 3:
        flag_2 = True
    elif h % 2 == 0:
        flag_2 = False
    else:
        for d in range(3,int(math.sqrt(h))+1,2):
            if h % d == 0:
                flag_2 = False
                break
    if flag_2:
        so_nguyen_lon_hon_n = h
        break
# In ra màn hình:
if flag:
    print(f"{n} là số  nguyên tố")
else:
    print(f"{n} không phải số nguyên tố, số nguyên tố < {n} là: {so_nguyen_nho_n}")
    print(f"{n} không phải số nguyên tố, số nguyên tố > {n} là: {so_nguyen_lon_hon_n}")
    



        
                    



    

    
