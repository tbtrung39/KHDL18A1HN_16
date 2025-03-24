Str= input("Nhập chuỗi:")
number_str=""
for c in Str:
    if c.isdigit():
        number_str+=c
if number_str =="":
    print('Chuỗi không chứa số nào')
else:
    number = int(number_str)
    print("chuỗi số sau khi lọc:",number)
    tong_uoc=0
    for i in range(1,number):
        if number % i ==0:
            tong_uoc +=1
    if tong_uoc == number:
        print(number,"là số hoàn hảo")
    else:
        print(number,"không phải là số hoàn hảo")