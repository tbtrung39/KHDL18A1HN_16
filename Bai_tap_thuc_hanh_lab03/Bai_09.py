import math
n = int(input("Nhập n: "))
thua_so = 0
thua_so_nguyen_to = 0
for i in range(1,n+1):
    flag = True
    if n % i == 0:
        thua_so = i
        if thua_so <= 1:
            flag = False
        elif thua_so == 2 or i == 3:
            flag = True
        elif thua_so % 2 == 0:
            flag = False
        else: 
            for j in range(3,int(math.sqrt(thua_so))+1,2):
                if thua_so % j == 0:
                    flag = False
                    break
        if flag :
            thua_so_nguyen_to = thua_so
            print(f"Các thừ số nguyên tố của {n} là: {thua_so_nguyen_to}")

    
        