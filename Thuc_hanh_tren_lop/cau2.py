#c1
Str = input("Nhập chuỗi: ")
count = 0
for char in Str:
    if not (char.isalpha() or char.isdigit()):
        count += 1
print("Số ký tự không phải là chữ cái và không phải là số là:", count)

###c2
Str = input("Nhập chuỗi: ")
count = len(list(filter(lambda char: not (char.isalpha() or char.isdigit()), Str)))
print("Số ký tự không phải là chữ cái và không phải là số là:", count)

