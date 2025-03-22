#Cach 1:
Str = input("Nhập chuỗi: ")
count = 0
for ky_tu in Str:
    if not ky_tu.isalnum():
        count += 1
print("Số ký tự không phải chữ cái và số là:", count)


#Cach2:
Str = input("Nhập chuỗi: ")
so = 0
for c in str:
    if '0' <= c <= '9':
        so += 1
print("Số chữ số trong chuỗi:", so)