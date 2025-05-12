def tim_so_chung(tep_m, tep_n, tep_chung):
    with open(tep_m, 'r') as f_m:
        so_m = {int(line.strip()) for line in f_m}
    with open(tep_n, 'r') as f_n:
        so_n = {int(line.strip()) for line in f_n}
    so_chung_set = so_m.intersection(so_n)
    so_chung_list = sorted(list(so_chung_set))
    with open(tep_chung, 'w') as f_chung:
        for so in so_chung_list:
            f_chung.write(str(so) + '\n')
    print(f"Các số chung đã được lưu vào tệp '{tep_chung}':")
    with open(tep_chung, 'r') as f_chung:
        for line in f_chung:
            print(line.strip())
ten_tep_m = 'KHDL18A1HN_16/baitapthuchanhlab11/bai7/m_num.txt'
ten_tep_n = 'KHDL18A1HN_16/baitapthuchanhlab11/bai7/n_num.txt'
ten_tep_chung = 'KHDL18A1HN_16/baitapthuchanhlab11/bai7/so_chung.txt'
tim_so_chung(ten_tep_m, ten_tep_n, ten_tep_chung)