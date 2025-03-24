Str = input("Nhập chuỗi ký tự: ")
count = sum(1 for c in Str if c.isdigit())
print("Số ký tự là số trong chuỗi:", count)