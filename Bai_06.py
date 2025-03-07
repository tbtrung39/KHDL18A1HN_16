n = int(input("Nhập số bất kì: "))
str_num = ""

while True:
    n1 = n % 10
    if n1 == 0:
        str_num += "không"
    elif n1 == 1:
        str_num = "một " + str_num
    elif n1 == 2:
        str_num = "hai " + str_num
    elif n1 == 3:
        str_num = "ba " + str_num
    elif n1 == 4:
        str_num = "bốn " + str_num
    elif n1 == 5:
        str_num = "năm " + str_num
    elif n1 == 6:
        str_num = "sáu " + str_num
    elif n1 == 7:
        str_num = "bảy " + str_num
    elif n1 == 8:
        str_num = "tám " + str_num
    elif n1 == 9:
        str_num = "chín " + str_num
    n = n // 10
    if n == 0:
        break
print(str_num)
    
