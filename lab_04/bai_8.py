
c=input("Nhap mot ky tu: ")
while len(c)!=1:
    print("Vui long nhap dung mot ky tu")
    c=input("Nhap mot ky tu: ")
print(f"Gia tri ASCII cua {c} la: {ord(c)}")
