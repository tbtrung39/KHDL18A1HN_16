# Tạo từ điển nhân viên
dsnv = {}

# b. Thêm nhân viên (thêm 2 người ví dụ)
i = 0
while i < 2:
    print("\nThêm nhân viên", i + 1)
    ma = input("Mã nhân viên: ")
    ten = input("Họ tên: ")
    nam_sinh = int(input("Năm sinh: "))
    luong = int(input("Lương: "))
    dsnv[ma] = [ten, nam_sinh, luong]
    i += 1

# c. Tìm nhân viên theo mã x
x = input("\nNhập mã nhân viên cần tìm: ")
tim_thay = False
for ma in dsnv:
    if ma == x:
        print("Thông tin nhân viên:")
        print("Tên:", dsnv[ma][0], "| Năm sinh:", dsnv[ma][1], "| Lương:", dsnv[ma][2])
        tim_thay = True
        break
if not tim_thay:
    print("Không tìm thấy nhân viên.")

# d. Tăng lương 1000000 cho nhân viên mã y
y = input("\nNhập mã nhân viên cần tăng lương: ")
for ma in dsnv:
    if ma == y:
        dsnv[ma][2] += 1000000
        print("Đã tăng lương cho nhân viên", dsnv[ma][0])

# e. Xóa nhân viên mã z
z = input("\nNhập mã nhân viên cần xóa: ")
dsnv_moi = {}
for ma in dsnv:
    if ma != z:
        dsnv_moi[ma] = dsnv[ma]
dsnv = dsnv_moi

# f. Sắp xếp theo năm sinh giảm dần
# Đưa ra danh sách để sort
ds = []
for ma in dsnv:
    ds.append((ma, dsnv[ma][0], dsnv[ma][1], dsnv[ma][2]))

# Bubble sort theo năm sinh
i = 0
while i < len(ds) - 1:
    j = 0
    while j < len(ds) - i - 1:
        if ds[j][2] < ds[j+1][2]:
            tmp = ds[j]
            ds[j] = ds[j+1]
            ds[j+1] = tmp
        j += 1
    i += 1

print("\nDanh sách nhân viên theo năm sinh giảm dần:")
for nv in ds:
    print("Mã:", nv[0], "| Tên:", nv[1], "| Năm sinh:", nv[2], "| Lương:", nv[3])