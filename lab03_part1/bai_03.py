n = int(input("Nhập số n: "))
dem_uoc = 0  

for i in range(1, n + 1):
    if n % i == 0:
        dem_uoc += 1

if dem_uoc == 2:  
    print(n, "là số nguyên tố.")
else:
    print(n, "không phải số nguyên tố.")

    
    for gan_nhat in range(n - 1, 1, -1):
        dem_uoc_gan_nhat = 0

        for j in range(1, gan_nhat + 1):
            if gan_nhat % j == 0:
                dem_uoc_gan_nhat += 1
        
        if dem_uoc_gan_nhat == 2:  
            print("Số nguyên tố gần nhất nhỏ hơn", n, "là:", gan_nhat)
            break
