menu = {
    1: "Cafe",
    2: "Cam vắt",
    3: "Nước ép cà rốt",
    4: "Nước lọc",
    5: "Nước dừa"
}
print("Menu đồ uống:")
ma_so = 1
while ma_so <= 5:
    ten_do_uong = menu[ma_so]
    print(f"{ma_so}. {ten_do_uong}")
    ma_so += 1

while True:
    lua_chon = int(input("Chọn đồ uống (1-5): "))
    hop_le = 0
    ma_so = 1
    while ma_so <= 5:
        if lua_chon == ma_so:
            hop_le = 1 
            break
        ma_so += 1
    if hop_le:
        print(f"Bạn đã chọn: {menu[lua_chon]}")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")