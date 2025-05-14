import math
def tim_uoc_so_nguyen_to(n):
    uoc_so_nguyen_to = set()
    while n % 2 == 0:
        uoc_so_nguyen_to.add(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            uoc_so_nguyen_to.add(i)
            n //= i
    if n > 2:
        uoc_so_nguyen_to.add(n)
    return sorted(list(uoc_so_nguyen_to))
def xu_ly_tep(tep_in, tep_out):
    with open(tep_in, 'r') as f_in, open(tep_out, 'w') as f_out:
        for line in f_in:
            so = int(line.strip())
            uoc_so = tim_uoc_so_nguyen_to(so)
            f_out.write(' '.join(map(str, uoc_so)) + '\n')
ten_tep_in = 'KHDL18A1HN_16/baitapthuchanhlab11/bai4/f_in.dat'
ten_tep_out = 'KHDL18A1HN_16/baitapthuchanhlab11/bai4/f_out.dat'
xu_ly_tep(ten_tep_in, ten_tep_out)