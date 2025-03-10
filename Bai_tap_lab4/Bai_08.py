
character = input("Nhập một ký tự: ")  
if len(character) == 1:   
    ascii_value = ord(character)  
    print("Giá trị ASCII của ký tự '{}' là: {}".format(character, ascii_value))  
else:  
    print("Vui lòng chỉ nhập một ký tự.")  