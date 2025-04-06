tap_hop_a_hon_hop = {1, 3.14, "hello", 5, "world", 2.71, -2, "python"}
so_nguyen = 0
so_thuc = 0
chuoi_ky_tu = 0
for phan_tu in tap_hop_a_hon_hop:
    if isinstance(phan_tu, int):
        so_nguyen += 1
    elif isinstance(phan_tu, float):
        so_thuc += 1
    elif isinstance(phan_tu, str):
        chuoi_ky_tu += 1
print("Tập hợp A hỗn hợp:", tap_hop_a_hon_hop)
print("Số phần tử là số nguyên:", so_nguyen)
print("Số phần tử là số thực:", so_thuc)
print("Số phần tử là chuỗi ký tự:", chuoi_ky_tu)