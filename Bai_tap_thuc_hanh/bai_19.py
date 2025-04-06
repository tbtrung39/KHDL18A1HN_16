nv = {}

while True:
    print("\nChọn thao tác:")
    print("a. Tạo từ điển.")
    print("b. Thêm nhân viên.")
    print("c. Tìm kiếm nhân viên theo lương.")
    print("d. Tăng lương.")
    print("e. Xóa nhân viên.")
    print("f. Sắp xếp theo lương giảm dần.")
    print("g. Thoát.")
    chon = input("Nhập lựa chọn (a - g): ")

    if chon == "a":
        nv = {}
        print("Từ điển nhân viên đã được tạo.")

    elif chon == "b":
        ma = input("Nhập mã nhân viên: ")
        ten = input("Nhập tên nhân viên: ")
        tuoi = int(input("Nhập tuổi: "))
        luong = int(input("Nhập lương: "))
        nv[ma] = [ten, tuoi, luong]
        print("Đã thêm nhân viên.")

    elif chon == "c":
        l = int(input("Nhập mức lương cần tìm: "))
        print("Nhân viên có lương là", l, ":")
        for ma in nv:
            if nv[ma][2] == l:
                print(ma, ":", nv[ma])

    elif chon == "d":
        ma = input("Nhập mã nhân viên cần tăng lương: ")
        if ma in nv:
            tang = int(input("Nhập số tiền tăng: "))
            nv[ma][2] += tang
            print("Đã tăng lương.")
        else:
            print("Không tìm thấy nhân viên.")

    elif chon == "e":
        ma = input("Nhập mã nhân viên cần xóa: ")
        if ma in nv:
            del nv[ma]
            print("Đã xóa nhân viên.")
        else:
            print("Không tìm thấy.")

    elif chon == "f":
        sap = sorted(nv.items(), key=lambda x: x[1][2], reverse=True)
        print("Danh sách nhân viên theo lương giảm dần:")
        for item in sap:
            print(item[0], ":", item[1])

    elif chon == "g":
        print("Kết thúc chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ.")
