n=int(input("Nhập n:"))
print("các sô hoàn hảo hảo nhỏ nhơn n là:")
for num in range(2,n):
    tong_uoc=0
    for i in range(1,num):
        if num % i == 0:
            tong_uoc +=i
    if tong_uoc==num:
        print(num)

    