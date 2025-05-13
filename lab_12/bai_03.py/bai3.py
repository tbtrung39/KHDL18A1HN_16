try:
    path = input("Nhap duong dan den file can doc: ")
    with open(path, 'r', encoding='utf-8') as file:
        nd = file.read()
    with open('copy.dat', 'w', encoding='utf-8') as copy_file:
        copy_file.write(nd)
    print("Da sao chep noi dung sang file 'copy.dat'.")
except FileNotFoundError:
    print("Khong tim thay file. Ket thuc chuong trinh.")