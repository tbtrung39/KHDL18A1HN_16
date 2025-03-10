n = int(input("Nhap so nguyen duong n bat ki: "))

while n < 0:
    print("Vui long nhap so khong am")
    n = int(input("Nhap so nguyen duong n: "))

for so in str(n):
    if so == "0":
        print("không", end=" ")
    elif so == "1":
        print("một", end=" ")
    elif so == "2":
        print("hai", end=" ")
    elif so == "3":
        print("ba", end=" ")
    elif so == "4":
        print("bốn", end=" ")
    elif so == "5":
        print("năm", end=" ")
    elif so == "6":
        print("sáu", end=" ")
    elif so == "7":
        print("bảy", end=" ")
    elif so == "8":
        print("tám", end=" ")
    elif so == "9":
        print("chín", end=" ")

print()