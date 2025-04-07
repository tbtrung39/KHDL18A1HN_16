nv = {}
while True:
    chon = input("Chọn thao tác (a-f, ESC để thoát): ")
    if chon == 'a':
        nv = {}
    elif chon == 'b':
        ma = input("Mã NV: ")
        ten = input("Tên: ")
        ns = int(input("Năm sinh: "))
        luong = int(input("Lương: "))
        nv[ma] = {"ten": ten, "ns": ns, "luong": luong}
    elif chon == 'c':
        x = input("Mã cần tìm: ")
        print(nv.get(x, "Không tìm thấy"))
    elif chon == 'd':
        y = input("Mã cần tăng lương: ")
        if y in nv:
            nv[y]["luong"] += 1000000
    elif chon == 'e':
        z = input("Mã cần xóa: ")
        if z in nv:
            del nv[z]
    elif chon == 'f':
        sx = sorted(nv.items(), key=lambda x: x[1]["ns"])
        print(sx)
    elif chon.upper() == "ESC":
        break
