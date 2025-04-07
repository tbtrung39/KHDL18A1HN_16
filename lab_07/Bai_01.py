
tap_hop=set()
print("Nhap ky tu(nhap 'ESC' de dung): ")
while True:
    kt=input("Nhap ky tu: ")
    if kt=="ESC":
        break
    tap_hop.add(kt)
for kt in list(tap_hop):
    if kt.isdigit():
        tap_hop.remove(kt)
print("Taphop sau khi xoa cac ky tu so:",tap_hop)
