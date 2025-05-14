def tinh_tong_so_le(ten_tep):
    tong_le = 0
    with open(ten_tep, 'r') as f:
        for dong in f:
            cac_so_str = dong.strip().split()
            for so_str in cac_so_str:
                so = int(so_str)
                if so % 2 != 0:
                    tong_le += so
    return tong_le
ten_tep_dayso = 'KHDL18A1HN_16/baitapthuchanhlab11/bai1/dayso.dat'
tong = tinh_tong_so_le(ten_tep_dayso)
print(f"Tổng các số lẻ trong tệp '{ten_tep_dayso}' là: {tong}")