n = input("Nhap so duong n bat ki: ")

while float(n) < 0:
    print("Vui long nhap so khong am")
    n = input("n= ")

for so in str(n):
    if so == "0":
        print("khong", end=" ")
    elif so == "1":
        print("mot", end=" ")
    elif so == "2":
        print("hai", end=" ")
    elif so == "3":
        print("ba", end=" ")
    elif so == "4":
        print("bon", end=" ")
    elif so == "5":
        print("nam", end=" ")
    elif so == "6":
        print("sau", end=" ")
    elif so == "7":
        print("bay", end=" ")
    elif so == "8":
        print("tam", end=" ")
    elif so == "9":
        print("chin", end=" ")
    elif so==".":
        print("cham",end=" ")

print()