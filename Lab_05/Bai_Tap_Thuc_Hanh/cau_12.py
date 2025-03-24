s = input("Nhập chuỗi: ")
words, temp = [], ""
for c in s:
    if c.isalnum():
        temp += c
    elif temp:
        words.append(temp)
        temp = ""
if temp:
    words.append(temp)
print("Các từ trong chuỗi:", words)