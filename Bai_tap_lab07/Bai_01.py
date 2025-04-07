s = set()
while True:
    char = input("Nhập ký tự (ESC để kết thúc): ")
    if char == '\x1b':  
        break
    s.add(char)

digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
s = s - digits

print("Tập hợp sau khi xóa ký tự số:", s)