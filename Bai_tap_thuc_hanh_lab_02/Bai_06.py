num = int(input("Nhập số nguyên có ba chữ số: "))
if num >= 100 or num <= -100:
    a = num // 100
    b = num % 100
    c = b // 10
    d = b % 10
    print(f"Cách đọc số {num} là: {a} trăm {c} mươi {d}")