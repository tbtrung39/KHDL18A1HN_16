n = int(input("Nhap gia tri n:"))
print("Cac so hoan hao nho hon",n,"la:")
for num in range(2,n):
    tong_uoc_so = 0
    for i in range(1,num):
        if num % i == 0 :
            tong_uoc_so += i
    if tong_uoc_so == num:
        print(num)
        
