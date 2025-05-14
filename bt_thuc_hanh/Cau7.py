# Cau 7
def tim_so_chung():
    try:
        with open('m_num.txt', 'x') as f:
            f.write("2 3 5 7 11 13")
    except FileExistsError:
        pass
    
    try:
        with open('n_num.txt', 'x') as f:
            f.write("1 2 3 4 5 6 7 8")
    except FileExistsError:
        pass
    with open('m_num.txt', 'r') as f1, open('n_num.txt', 'r') as f2:
        m_numbers = set(map(int, f1.read().split()))
        n_numbers = set(map(int, f2.read().split()))
    so_chung = sorted(m_numbers & n_numbers)
    with open('so_chung.txt', 'w') as f:
        f.write(' '.join(map(str, so_chung)))
    with open('so_chung.txt', 'r') as f:
        print("Các số có mặt ở cả 2 file:")
        print(f.read())

tim_so_chung()