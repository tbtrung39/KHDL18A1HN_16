Str = input("Nhập chuỗi ký tự: ")
max_substr = ""
current_substr = ""
i = 0
while i < len(Str):
    current_substr = Str[i]
    i += 1
    while i < len(Str) and Str[i] == Str[i-1]:
        current_substr += Str[i]
        i += 1
    if len(current_substr) > len(max_substr):
        max_substr = current_substr
print(f"Chuỗi con có độ dài cực đại: {max_substr}")
