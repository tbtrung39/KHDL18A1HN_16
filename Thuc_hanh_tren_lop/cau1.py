char_set = set()
print("Nhập các ký tự. Nhấn 'ESC' để kết thúc.")
while True:
    char = input("Nhập ký tự: ")
    if char == 'ESC':
        break
    if char.isdigit(): 
        continue
    char_set.add(char)
print(f"Tập hợp sau khi xóa các số: {char_set}")