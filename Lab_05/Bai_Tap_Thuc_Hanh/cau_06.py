s = input("Nhập chuỗi: ")
hex = "0123456789ABCDEFabcdef"
f = ""
for c in s:
    if c in hex:
        f += c
if len(f) == len(s):
    print("Là chuỗi Hex")
else:
    decimal = int(f, 16) if f else 0
    print("Chuyển sang thập phân:", decimal)