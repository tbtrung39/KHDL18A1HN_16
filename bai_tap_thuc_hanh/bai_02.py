Str =  input("Nhập chuỗi:") 
dem = 0
for c in Str:
    if not c.isalnum():
        dem+=1
print("Số ký tự không phải là chữ cái tiếng Anh và không là số trong chuỗi là:",dem)