str = input("Nhập chuỗi ký tự: ")
str1 = ""
tong = 0
for i in str:
    flag = True
    if i.isdigit():
        str1 = str1 + i
        flag = True
    else:
        flag = False
if flag :
    print(f"Chuỗi là ký tự số là: {str1}")
    n = int(str1)
    for k in range(1,n):
        if n % k == 0:
            tong += k
    if tong == n:
        print(f"{n} là số hoàn hảo")
    else:
        print(f"{n} không phải số hoàn hảo")
else:
    print("Chuỗi không có ký tự nào là số")
    
