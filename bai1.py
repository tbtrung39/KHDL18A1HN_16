tap_ky_tu = set()

print("Nhập ký tự (gõ 'ESC' để kết thúc):")
while True:
    ky_tu = input("Nhập ký tự: ")
    if ky_tu == "ESC":
        break
    tap_ky_tu.add(ky_tu)

print("Tập ký tự sau khi loại trùng:", tap_ky_tu)
