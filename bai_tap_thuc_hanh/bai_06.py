Str= input("Nhập chuỗi:")
hex_digits= "0123456789ABCDEFabcdef"
filtered_str = ""
for c in Str:
    if c in hex_digits:
        filtered_str +=c
if filtered_str == Str:
    print("Chuỗi là hệ hex không hợp lệ")
else:
    if filtered_str =="":
        print("Chuỗi không có hex")
    else:
        decimal_value = int(filtered_str,16)
        print("Chuỗi sau khi lọc:",filtered_str)
        print("GIá trị thập phân :",decimal_value)