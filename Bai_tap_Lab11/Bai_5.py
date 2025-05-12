def ghep_phach_va_sap_xep():
    try:
        # Đọc dữ liệu từ các file
        sbd_phach = {}
        with open('Sbd_Ph.dat', 'r') as file:
            for line in file:
                a, b = map(int, line.strip().split())
                sbd_phach[a] = b
        
        sbd_ten = {}
        with open('Sbd_Ten.txt', 'r') as file:
            for line in file:
                parts = line.strip().split()
                a = int(parts[0])
                ten = ' '.join(parts[1:])
                sbd_ten[a] = ten
        
        phach_diem = {}
        with open('Phieu_Diem.txt', 'r') as file:
            for line in file:
                a, b = map(int, line.strip().split())
                phach_diem[a] = b
        
        # Ghép thông tin
        ket_qua = []
        for sbd in sbd_phach:
            phach = sbd_phach[sbd]
            ten = sbd_ten.get(sbd, "Không rõ")
            diem = phach_diem.get(phach, 0)
            ket_qua.append((sbd, ten, diem))
        
        # Sắp xếp theo điểm giảm dần
        ket_qua.sort(key=lambda x: x[2], reverse=True)
        
        # Ghi vào file
        with open('Ketqua.txt', 'w') as file:
            for item in ket_qua:
                file.write(f"{item[0]} {item[1]} {item[2]}\n")
        
        print("Đã ghi kết quả vào file Ketqua.txt")
    except FileNotFoundError as e:
        print(f"Không tìm thấy file: {e.filename}")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

ghep_phach_va_sap_xep()