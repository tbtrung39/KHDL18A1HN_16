chuoi_A = input("Nhập chuỗi A (gồm chữ và số): ")
chuoi_B = input("Nhập chuỗi B (gồm chữ và số): ")
tap_hop_A = set(chuoi_A)
tap_hop_B = set(chuoi_B)
phan_tu_chung = tap_hop_A.intersection(tap_hop_B)
print("Các phần tử chung của A và B là:")
for phan_tu in phan_tu_chung:
    print(phan_tu, end=' ')