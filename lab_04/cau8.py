while True:
    chu = input("Nhập một ký tự: ")
    if len(chu) == 1:  # Kiểm tra nhập đúng 1 ký tự
        break
    print("Vui lòng nhập một ký tự duy nhất!")
print(f"Giá trị ASCII của '{chu}' là {ord(chu)}")
