while True:
    print("_______Menu_______")
    print("1: Cafe")
    print("2: Cam vắt")
    print("3: Nước ép cà rốt")
    print("4: Nước lọc")
    print("5: Nước dừa")
    print("Bấm phím 0 nếu bạn không muốn order nữa!!")
    choice = input("Menu của bạn đây mời bạn gọi đồ uống: ")
    if choice == "1":
        print("Hệ thống xác nhận bạn order Cafe")
        print("Bạn có muốn gọi thêm gì nx không =)))")
    elif choice == "2":
        print("Hệ thống xác nhận bạn order Cam vắt")
        print("Bạn có muốn gọi thêm gì nx không =)))")
    elif choice == "3":
        print("Hệ thống xác nhận bạn order Nươc éo cà rốt")
        print("Bạn có muốn gọi thêm gì nx không =)))")
    elif choice == "4":
        print("Hệ thống xác nhận bạn order Nước lọc")
        print("Bạn có muốn gọi thêm gì nx không =)))")
    elif choice == "5":
        print("Hệ thống xác nhận bạn order Nước dừa")
        print("Bạn có muốn gọi thêm gì nx không =)))")
    elif choice == "0":
        print("Thank You!!!")
        break
    else:
        print("Vui lòng chọn nước có trong Menu, mời bạn nhập lại")
    