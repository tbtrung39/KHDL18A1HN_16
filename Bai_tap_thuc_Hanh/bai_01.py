char_set = set()
print("Nhập các ký tự (nhấn ESC để kết thúc):")
while True:
    char = input("Nhập ký tự: ")
    if len(char) == 1:
        if char == 'E':  
            break
        char_set.add(char)
    else:
        print("Vui lòng chỉ nhập một ký tự!")
print("Tập hợp ban đầu:", char_set)
char_set = {x for x in char_set if not x.isdigit()}
print("Tập hợp sau khi xóa ký tự số:", char_set)