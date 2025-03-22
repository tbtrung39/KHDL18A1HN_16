str1 = input("Nhập chuỗi: ")
từ = ""
for i in str1:
    if i != ' ' and i != ',':
        từ += i
    else:
        if từ != "":
            print(từ)
            từ = ""
if từ != "":
    print(từ)
