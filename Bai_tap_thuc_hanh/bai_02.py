Str = input('Nhập vào một chuỗi ký tự: ')
print('Chuỗi ký tự vừa nhập:', Str)
dem = 0  
for c in Str:
    if not ("0" <= c <= "9" or "A" <= c <= "Z" or "a" <= c <= "z"):
        dem += 1
print('Số ký tự không phải chữ cái tiếng Anh và không phải số trong chuỗi:', dem)
