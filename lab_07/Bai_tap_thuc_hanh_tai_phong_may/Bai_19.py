# a. Tạo mới từ điển
nhanvien = {}

# b. Nhập số lượng nhân viên
n = int(input("Nhập số lượng nhân viên: "))

# Nhập thông tin nhân viên
for i in range(n):
    print(f"\nNhập thông tin nhân viên thứ {i+1}:")
    ma = input("Mã nhân viên (4 chữ số): ")
    ten = input("Họ tên nhân viên (tối đa 20 ký tự): ")[:20]  # Giới hạn 20 ký tự
    ns = int(input("Năm sinh: "))
    luong = int(input("Lương: "))
    nhanvien[ma] = [ten, ns, luong]

# --- MENU chức năng ---
while True:
    print("\n========== MENU ==========")
    print("1. Thêm nhân viên")
    print("2. Tìm nhân viên theo mã")
    print("3. Tăng lương cho nhân viên")
    print("4. Xóa nhân viên theo mã")
    print("5. Sắp xếp nhân viên giảm dần theo năm sinh")
    print("0. Thoát")
    chon = input("Chọn chức năng: ")

    if chon == "1":
        # b. Thêm nhân viên
        ma = input("Mã nhân viên (4 chữ số): ")
        ten = input("Họ tên nhân viên (tối đa 20 ký tự): ")[:20]
        ns = int(input("Năm sinh: "))
        luong = int(input("Lương: "))
        nhanvien[ma] = [ten, ns, luong]
        print("Đã thêm nhân viên.")

    elif chon == "2":
        # c. Tìm kiếm nhân viên theo mã
        x = input("Nhập mã nhân viên cần tìm: ")
        if x in nhanvien:
            print("Thông tin nhân viên:")
            print("Họ tên:", nhanvien[x][0])
            print("Năm sinh:", nhanvien[x][1])
            print("Lương:", nhanvien[x][2])
        else:
            print("Không tìm thấy nhân viên.")

    elif chon == "3":
        # d. Tăng lương 1 triệu cho mã y
        y = input("Nhập mã nhân viên cần tăng lương: ")
        if y in nhanvien:
            nhanvien[y][2] += 1000000
            print("Đã tăng lương cho nhân viên", y)
        else:
            print("Không tìm thấy nhân viên.")

    elif chon == "4":
        # e. Xóa nhân viên theo mã z
        z = input("Nhập mã nhân viên cần xóa: ")
        if z in nhanvien:
            del nhanvien[z]
            print("Đã xóa nhân viên", z)
        else:
            print("Không tìm thấy nhân viên.")

    elif chon == "5":
        # f. Sắp xếp theo năm sinh giảm dần
        sapxep = sorted(nhanvien.items(), key=lambda x: x[1][1], reverse=True)
        print("Danh sách nhân viên (giảm dần theo năm sinh):")
        for ma, info in sapxep:
            print(f"Mã: {ma}, Họ tên: {info[0]}, Năm sinh: {info[1]}, Lương: {info[2]}")

    elif chon == "0":
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ.")