tnct = float(input("Nhập TNCT: "))
if tnct < 2 or tnct == 2:
    if tnct < 2:
        print("3.00")
    else:
        print("3.34")
elif tnct >= 3:
    print("3.99")
else:
    print("Không có thông tin cho 2 < TNCT < 3!")