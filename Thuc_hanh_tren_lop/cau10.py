#c1
Str1 = input("Nhập chuỗi Str1: ")
Str2 = input("Nhập chuỗi Str2: ")
max_substr = ""
for i in range(len(Str1)):
    for j in range(i + 1, len(Str1) + 1):
        substr = Str1[i:j]
        if substr in Str2 and len(substr) > len(max_substr):
            max_substr = substr
print(f"Chuỗi con chung có độ dài cực đại: {max_substr}")

##c2
Str1 = input("Nhập chuỗi Str1: ")
Str2 = input("Nhập chuỗi Str2: ")
max_substr = ""
for length in range(min(len(Str1), len(Str2)), 0, -1):
    for i in range(len(Str1) - length + 1):
        substr = Str1[i:i+length]
        if substr in Str2:
            max_substr = substr
            break
    if max_substr:
        break
print(f"Chuỗi con chung có độ dài cực đại: {max_substr}")
