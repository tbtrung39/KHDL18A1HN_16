char = input("Nhập một ký tự: ")
if len(char) == 1:
    i = 32  
    while i <= 127: 
        if chr(i) == char:  
            print(f"Giá trị ASCII của ký tự '{char}' là: {i}")
            break  
        i += 1  
else:
    print("Vui lòng chỉ nhập một ký tự duy nhất.")
