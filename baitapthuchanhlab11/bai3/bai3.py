def tim_va_luu_cuc_tri(tep_in, tep_out):
    with open(tep_in, 'r') as f_in:
        dong = f_in.readline().strip()
        day_so = [int(so) for so in dong.split()]
    cac_cuc_tri = []
    n = len(day_so)
    if n < 3:
        so_luong_cuc_tri = 0
    else:
        for i in range(1, n - 1):
            if (day_so[i - 1] < day_so[i] > day_so[i + 1]) or \
               (day_so[i - 1] > day_so[i] < day_so[i + 1]):
                cac_cuc_tri.append(day_so[i])
        so_luong_cuc_tri = len(cac_cuc_tri)
    with open(tep_out, 'w') as f_out:
        f_out.write(str(so_luong_cuc_tri) + '\n')
        f_out.write(' '.join(map(str, cac_cuc_tri)) + '\n')
    print(f"Đã tìm thấy {so_luong_cuc_tri} cực trị và lưu vào tệp '{tep_out}'.")
ten_tep_in = 'KHDL18A1HN_16/baitapthuchanhlab11/bai3/f_in.dat'
ten_tep_out = 'KHDL18A1HN_16/baitapthuchanhlab11/bai3/f_out.dat'
tim_va_luu_cuc_tri(ten_tep_in, ten_tep_out)