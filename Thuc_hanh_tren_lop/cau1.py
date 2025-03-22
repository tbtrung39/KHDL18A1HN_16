#c1
Str = input("Nhập chuỗi ký tự: ")
count = 0
for char in Str:
    if '0' <= char <= '9':
        count += 1
print(f"Số ký tự là số trong chuỗi: {count}")

##c2
Str = input("Nhập chuỗi ký tự: ")
count = sum(1 for char in Str if char.isdigit())
print(f"Số ký tự là số trong chuỗi: {count}")
