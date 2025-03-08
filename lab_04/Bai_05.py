
while True:
    so = int(input("Nhập một số nguyên (nhập số âm để dừng): "))
    if so < 0:
        print("Đã nhập số âm. Chương trình dừng lại.")
        break  
    else:
        print("Số vừa nhập là:", so)