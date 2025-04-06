my_set = set()
print("Nhập các ký tự (nhấn ESC để kết thúc):")
while True:
    char = input()
    if char == chr(27):  
        break
    my_set.add(char)

print("Set ban đầu:", my_set)

digits_to_remove = set()
for item in my_set:
    if '0' <= item <= '9':
        digits_to_remove.add(item)

for digit in digits_to_remove:
    my_set.remove(digit)

print("Set sau khi xóa ký tự số:", my_set)