def lay_chu_so_hang_tram(so):
    so = abs(so)
    if so < 100:
        return 0
    else:
        return (so // 100) % 10
try:
    so = int(input("Nhap vao mot so nguyen: "))
    chu_so_hang_tram = lay_chu_so_hang_tram(so)
    print(f"Chu so hang tram cua so {so} la: {chu_so_hang_tram}")
except ValueError:
    print("Vui long nhap mot so nguyen hop le.")