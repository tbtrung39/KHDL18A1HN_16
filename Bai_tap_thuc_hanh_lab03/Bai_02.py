n = int(input("Nhâp n: "))
sum = 0
for i in range(1,n):
    for j in range(1,i):
        if i % j == 0:
            sum+=j
    if sum == i :
        print(i)
    


