A = set(input("Nhập chuỗi ký tự: "))
so = {c for c in A if c.isdigit()}
chu = {c for c in A if c.isalpha()}
print("Số:", so)
print("Chữ:", chu)
