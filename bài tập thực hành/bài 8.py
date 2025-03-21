s = input("Nhập đoạn văn: ")
words = 1 if s else 0
for c in s:
    if c == ' ':
        words += 1
print("Số từ trong chuỗi:", words)