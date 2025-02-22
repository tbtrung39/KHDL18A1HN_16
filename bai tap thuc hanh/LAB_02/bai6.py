so = int(input("Nhập số nguyên có ba chữ số: "))
if so >= 100 or so <= -100:
    a = so // 100
    b = so % 100
    c = b // 10
    d = b % 10
    print(f"Cách đọc số {so} là: {a} trăm {c} mươi {d}")