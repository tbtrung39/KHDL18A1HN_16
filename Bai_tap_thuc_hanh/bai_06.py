so = input("Nhập một số: ")
i = 0
while i < len(so):
    if so[i] == '0':
        print("không", end=" ")
    elif so[i] == '1':
        print("một", end=" ")
    elif so[i] == '2':
        print("hai", end=" ")
    elif so[i] == '3':
        print("ba", end=" ")
    elif so[i] == '4':
        print("bốn", end=" ")
    elif so[i] == '5':
        print("năm", end=" ")
    elif so[i] == '6':
        print("sáu", end=" ")
    elif so[i] == '7':
        print("bảy", end=" ")
    elif so[i] == '8':
        print("tám", end=" ")
    elif so[i] == '9':
        print("chín", end=" ")
    i += 1  
print()
