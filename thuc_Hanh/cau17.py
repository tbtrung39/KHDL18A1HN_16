sv = {}
while True:
    msv = input("Nhập mã SV (ESC để thoát): ")
    if msv.upper() == "ESC": break
    ten = input("Họ tên: ")
    diem = round(float(input("Điểm: ")))
    sv[msv] = {"ten": ten, "diem": diem}

sorted_sv = sorted(sv.items(), key=lambda x: -x[1]["diem"])
print("SV sắp xếp giảm dần điểm:")
for x in sorted_sv:
    print(x)
