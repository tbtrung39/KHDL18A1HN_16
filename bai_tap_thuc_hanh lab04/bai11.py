while True:
    print("\nMenu đồ uống:")
    print("1. Cafe")
    print("2. Cam vắt")
    print("3. Nước ép cà rốt")
    print("4. Nước lọc")
    print("5. Nước dừa")
    print("0. Thoát")

    # Nhập lựa chọn từ người dùng
    lua_chon = input("Nhập số tương ứng với đồ uống bạn muốn gọi: ")

    # Kiểm tra nếu người dùng nhập "0" thì thoát chương trình
    if lua_chon == "0":
        print("Cảm ơn bạn! Hẹn gặp lại.")
        break
    elif lua_chon == "1":
        print("Bạn đã chọn Cafe.")
    elif lua_chon == "2":
        print("Bạn đã chọn Cam vắt.")
    elif lua_chon == "3":
        print("Bạn đã chọn Nước ép cà rốt.")
    elif lua_chon == "4":
        print("Bạn đã chọn Nước lọc.")
    elif lua_chon == "5":
        print("Bạn đã chọn Nước dừa.")
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")