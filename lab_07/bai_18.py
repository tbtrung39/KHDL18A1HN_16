danh_sach = {
    "01": {'Ho ten': "Nguyen Van A", 'Diem thi': 0.1},
    "02": {'Ho ten': "Nguyen B", 'Diem thi': 1.2},
    "03": {'Ho ten': "Tran Van C", 'Diem thi': 8.1},
    "04": {'Ho ten': "Tran D", 'Diem thi': 2.1},
    "05": {'Ho ten': "Pham Van E", 'Diem thi': 1.1}
}
SBD = input('Nhap SBD: ')
if SBD in danh_sach:
    print('Ho ten: ' + danh_sach[SBD]['Ho ten'])
    print('Diem thi: ' + str(danh_sach[SBD]['Diem thi']))
else:
    ho_ten = input('Nhap ho ten thi sinh: ')
    diem_thi = float(input('Nhap diem thi: '))
    danh_sach[SBD] = {'Ho ten': ho_ten, 'Diem thi': diem_thi}
    print('Da them thi sinh moi vao danh sach')