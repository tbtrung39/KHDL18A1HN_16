def validate_input(user_input):
    if not user_input.isalpha():
        raise ValueError("Lỗi ký tự !!!")
    
    for i in range(len(user_input) - 1):
        if user_input[i] == user_input[i + 1]:
            raise ValueError("Lỗi nhập liệu !!!")
    
    for i in range(len(user_input) - 3):
        if len(set(user_input[i:i+4])) == 1:
            raise ValueError("Lỗi nhập lặp lại !!!")
    
    words = [user_input[i:i+5] for i in range(len(user_input) - 4)]
    for word in words:
        if words.count(word) > 1:
            raise ValueError("Lỗi nhập trùng lặp !!!")

while True:
    try:
        user_input = input("Nhập chuỗi ký tự: ")
        validate_input(user_input)
        print("Dữ liệu hợp lệ:", user_input)
        break
    except ValueError as ve:
        print(ve)