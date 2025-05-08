def sinh_hoan_vi(dang_co, con_lai):
    if not con_lai:
        print(dang_co)
        return
    for i in range(len(con_lai)):
        sinh_hoan_vi(dang_co + [con_lai[i]], con_lai[:i] + con_lai[i+1:])
n = int(input("Nhập số tự nhiên n: "))
day_so = list(range(1, n + 1))
sinh_hoan_vi([], day_so)
