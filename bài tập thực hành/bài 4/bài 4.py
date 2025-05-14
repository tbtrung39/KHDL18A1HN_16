try:
    path = input("Nhap duong dan den file can doc: ")
    try:
        with open(path, 'r', encoding='utf-8') as f_in:
            nd = f_in.read()
    except FileNotFoundError:
        print("Khong tim thay file nguon.")
        exit()
    try:
        with open("f_out.dat", 'w', encoding='utf-8') as f_out:
            f_out.write(nd)
            print("Da ghi noi dung vao file 'f_out.dat'.")
    except IOError:
        print("Loi.")
        exit()

except Exception as e:
    print("Loi:", e)