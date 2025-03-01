n = int(input("Nhập số n: "))

print("Các số nguyên tố nhỏ hơn hoặc bằng", n, "là:", end=" ")

for so in range(2, n + 1):  
    dem_uoc_so = 0  

    for uoc in range(1, so + 1): 
        if so % uoc == 0:
            dem_uoc_so += 1

    if dem_uoc_so == 2:  
        print(so, end=" ")
