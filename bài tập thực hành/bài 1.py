s = input("Nhập chuỗi: ")
so = 0
for c in s:
    if '0' <= c <= '9':
        so += 1
print("Số chữ số trong chuỗi:", so)