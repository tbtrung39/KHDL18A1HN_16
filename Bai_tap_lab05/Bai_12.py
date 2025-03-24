str1 = input("Nhập chuỗi: ")
tam = ""
i = 0
while i < len(str1):
    if str1[i] == ' ' or str1[i] == ',':
        if len(tam) > 0:
            print(tam)
            tam = ""
    else:
        tam += str1[i]
    i += 1

if len(tam) > 0:
    print(tam)