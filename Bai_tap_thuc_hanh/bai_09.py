str_input = input("Nhập chuỗi ký tự: ")
max_length = 1
current_length = 1
max_char = str_input[0]
for i in range(1, len(str_input)):
    if str_input[i] == str_input[i - 1]:
        current_length += 1
        if current_length > max_length:
            max_length = current_length
            max_char = str_input[i]
    else:
        current_length = 1
result = ""
for i in range(max_length):
    result += max_char

print("Chuỗi ký tự dài nhất là:", result)
