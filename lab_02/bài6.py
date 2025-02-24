def doc_so_ba_chu_so(so):
    hang_tram = ["", "Mot tram", "Hai tram", "Ba tram", "Bon tram", "Nam tram", "Sau tram", "Bay tram", "Tam tram", "Chin tram"]
    hang_chuc = ["", "Muoi", "Hai muoi", "Ba muoi", "Bon muoi", "Nam muoi", "Sau muoi", "Bay muoi", "Tam muoi", "Chin muoi"]
    hang_don_vi = ["", "Mot", "Hai", "Ba", "Bon", "Nam", "Sau", "Bay", "Tam", "Chin"]
    tram = so // 100
    chuc = (so % 100) // 10
    don_vi = so % 10
    if chuc == 0 and don_vi != 0:
        return f"{hang_tram[tram]} linh {hang_don_vi[don_vi]}"
    elif chuc == 0 and don_vi == 0:
        return f"{hang_tram[tram]}"
    else:
        return f"{hang_tram[tram]} {hang_chuc[chuc]} {hang_don_vi[don_vi]}"
try:
    so = int(input("Nhap vao mot so nguyen co ba chu so: "))
    if 100 <= so <= 999:
        print(f"Cach doc so {so} la: {doc_so_ba_chu_so(so)}")
    else:
        print("Vui long nhap mot so nguyen co ba chu so.")
except ValueError:
    print("Vui long nhap mot so nguyen hop le.")