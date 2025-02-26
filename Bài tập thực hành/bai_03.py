n=int(input("Nhập n:"))
so_nguyen_to=True
if n<2:
    so_nguyen_to= False
else:
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            so_nguyen_to= False
            break
if so_nguyen_to:
    print(n,"là só nguyên tố")
else:
    print(n,"không phải là số nguyên tố")
    so_be_hon_n = 0
    for i in range(n-1,1,-1):
        so_nguyen_to = True
        for j in range(2,int(i**0.5)+1):
            if i % j ==0:
             so_nguyen_to =False
            break
    so_lon_hon_n = 0
    for i in range(n+1,n+100):
        so_nguyen_to = True
        for j in range(2,int(i**0.5)+1):
            if i%j ==0:
                so_nguyen_to = False
                break
        if so_nguyen_to:
            so_lon_hon = 1
            break
    if so_be_hon_n and so_lon_hon_n :
     if (n - so_be_hon_n)<= (so_lon_hon_n - n):
        print("số nguyên tố gần nhất là:",so_be_hon_n)
     else:
        print("số nguyen tố gần nhất là :",so_lon_hon_n)
    elif so_be_hon_n:
     print("số nguyên tố gần nhất là:",so_be_hon_n)
    else:
     print("số nguyên tố gần nhất là:",so_lon_hon_n)

