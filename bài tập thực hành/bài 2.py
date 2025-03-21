s = input("Nhập chuỗi: ")
result = ""
for c in s:
    if '0' <= c <= '9':
        result += c
print("Chuỗi chỉ chứa số:", result)