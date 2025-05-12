import math
def doc_so_tu_tep(ten_tep):
    with open(ten_tep, 'r') as f:
        dong = f.readline().strip()
        cac_so_str = dong.split()
        return [int(so) for so in cac_so_str]
def la_tap_con(day_a, day_b, day_c):
    for a_i in day_a:
        thoa_man = False
        min_abs_diff_b = float('inf')
        for b_j in day_b:
            min_abs_diff_b = min(min_abs_diff_b, abs(a_i - b_j))
        min_abs_diff_c = float('inf')
        for c_k in day_c:
            min_abs_diff_c = min(min_abs_diff_c, abs(a_i - c_k))
        if min_abs_diff_b < min_abs_diff_c:
            thoa_man = True
        else:
            if min_abs_diff_b <= min_abs_diff_c:
                ton_tai_nho_hon = False
                for b_j in day_b:
                    if abs(a_i - b_j) < min_abs_diff_c:
                        ton_tai_nho_hon = True
                        break
                if ton_tai_nho_hon:
                    thoa_man = True
        if not thoa_man:
            return False
    return True 
ten_tep_inp = 'KHDL18A1HN_16/baitapthuchanhlab11/bai2/inp.txt'
ten_tep_out = 'KHDL18A1HN_16/baitapthuchanhlab11/bai2/out.dat'
ten_tep_fin = 'KHDL18A1HN_16/baitapthuchanhlab11/bai2/f_in.dat'
day_b = doc_so_tu_tep(ten_tep_inp)
day_c = doc_so_tu_tep(ten_tep_out)
day_a = doc_so_tu_tep(ten_tep_fin)
if la_tap_con(day_a, day_b, day_c):
    print(f"Dãy số trong '{ten_tep_fin}' là tập con theo định nghĩa.")
else:
    print(f"Dãy số trong '{ten_tep_fin}' KHÔNG phải là tập con theo định nghĩa.")