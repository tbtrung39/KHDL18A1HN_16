gioi_han = 10000
for num in range(1, gioi_han + 1):  
    tong_uoc = 0  
    for i in range(1, num):  
        if num % i == 0:  
            tong_uoc += i  

    if tong_uoc == num:   
        print(num)  