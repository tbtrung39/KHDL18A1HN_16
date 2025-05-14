def doc_du_lieu(ten_tep):
    du_lieu = {}
    with open(ten_tep, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split()
            if parts:
                key = int(parts[0])
                value = parts[1] if len(parts) == 2 else ' '.join(parts[1:])
                du_lieu[key] = value
    return du_lieu

def doc_phach_diem(ten_tep):
    du_lieu = {}
    with open(ten_tep, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split()
            key = int(parts[0])
            value = int(parts[1])
            du_lieu[key] = value
    return du_lieu

def ghep_thong_tin(sbd_phach, sbd_ten, phach_diem):
    thong_tin_thi_sinh = {}
    for sbd, phach in sbd_phach.items():
        ho_ten = sbd_ten[sbd]
        diem = phach_diem[phach]
        thong_tin_thi_sinh[sbd] = {
            'ho_ten': ho_ten,
            'diem': diem
        }
    return thong_tin_thi_sinh
def sap_xep_va_ghi_ket_qua(thong_tin_thi_sinh, tep_ket_qua):
    danh_sach_sap_xep = sorted(thong_tin_thi_sinh.items(), key=lambda item: item[1]['diem'], reverse=True)
    with open(tep_ket_qua, 'w', encoding='utf-8') as f:
        for sbd, info in danh_sach_sap_xep:
            f.write(f"{sbd}\t{info['ho_ten']}\t{info['diem']}\n")
    print(f"Đã ghép thông tin, sắp xếp và ghi kết quả vào tệp '{tep_ket_qua}'.")
tep_sbd_phach = 'KHDL18A1HN_16/baitapthuchanhlab11/bai5/Sbd_Ph.dat'
tep_sbd_ten = 'KHDL18A1HN_16/baitapthuchanhlab11/bai5/Sbd_Ten.txt'
tep_phieu_diem = 'KHDL18A1HN_16/baitapthuchanhlab11/bai5/Phieu_Diem.txt'
tep_ket_qua = 'KHDL18A1HN_16/baitapthuchanhlab11/bai5/Ketqua.txt'
sbd_phach = doc_du_lieu(tep_sbd_phach)
sbd_ten = doc_du_lieu(tep_sbd_ten)
phach_diem = doc_phach_diem(tep_phieu_diem)
thong_tin_thi_sinh = ghep_thong_tin(sbd_phach, sbd_ten, phach_diem)
sap_xep_va_ghi_ket_qua(thong_tin_thi_sinh, tep_ket_qua)