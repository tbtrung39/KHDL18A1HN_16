nhan_vien = {}
while True:
    print("\n=== MENU ===")
    print("1. Them nhan vien")
    print("2. Tim kiem nhan vien")
    print("3. Tang luong nhan vien")
    print("4. Xoa nhan vien")
    print("5. Sap xep tu dien giam dan theo nam sinh")
    print("6. Thoat")
    lua_chon = int(input("Nhap lua chon cua ban: "))
    if lua_chon == 1:
        ma_nv = input("Nhap ma nhan vien (4 ky tu): ")
        ho_ten = input("Nhap ho ten nhan vien (toi da 20 ky tu): ")
        nam_sinh = int(input("Nhap nam sinh nhan vien: "))
        luong = float(input("Nhap luong nhan vien: "))
        nhan_vien[ma_nv] = {"ho_ten": ho_ten, "nam_sinh": nam_sinh, "luong": luong}
    elif lua_chon == 2:
        x = input("Nhap ma nhan vien can tim: ")
        if x in nhan_vien:
            print(f"Thong tin nhan vien: {nhan_vien[x]}")
        else:
            print("Ma nhan vien khong ton tai.")
    elif lua_chon == 3:
        y = input("Nhap ma nhan vien can tang luong: ")
        if y in nhan_vien:
            nhan_vien[y]["luong"] += 1000000
            print(f"Luong moi cua nhan vien {y}: {nhan_vien[y]['luong']}")
        else:
            print("Ma nhan vien khong ton tai.")
    elif lua_chon == 4:
        z = input("Nhap ma nhan vien can xoa: ")
        if z in nhan_vien:
            del nhan_vien[z]
            print(f"Da xoa nhan vien co ma {z}")
        else:
            print("Ma nhan vien khong ton tai.")
    elif lua_chon == 5:
        sorted_nhan_vien = dict(sorted(nhan_vien.items(), key=lambda item: item[1]["nam_sinh"], reverse=True))
        print("Tu dien sau khi sap xep giam dan theo nam sinh:")
        for ma_nv, info in sorted_nhan_vien.items():
            print(f"{ma_nv}: {info}")
    elif lua_chon == 6:
        print("Ket thuc chuong trinh.")
        break
    else:
        print("Lua chon khong hop le. Vui long chon lai.")