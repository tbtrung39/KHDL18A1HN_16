Str=input('Nhập vào một chuỗi kí tự:')
print('Chuỗi kí tự vừa nhập:')
dem=0
for c in Str:
    if "0" <= c <= "9":
        dem+=1
print('Số kí tự là số trong chuỗi đã nhập là: ',dem)