tap_hop = set()
print("Nhap ky tu (nhap 'ESC' de ket thuc):")
while True:
    ky_tu = input("Nhap ky tu: ")
    if ky_tu == 'ESC':
        break
    tap_hop.add(ky_tu)
for ky_tu in list(tap_hop):
    if ky_tu.isdigit():
        tap_hop.remove(ky_tu)
print("Tap hop sau khi xoa cac ky tu so:", tap_hop)