def xu_ly_bang_so_khong_try(tep_du_lieu, tep_odd):
    with open(tep_du_lieu, 'r') as f:
        dongs = f.readlines()
    if len(dongs) >= 1:
        print("Dòng đầu tiên:", dongs[0].strip())
    if len(dongs) >= 3:
        print("Dòng thứ ba:", dongs[2].strip())
    print("\nNội dung toàn bộ file:")
    for dong in dongs:
        print(dong.strip())
    so_le = []
    for dong in dongs:
        cac_so = dong.strip().split()
        for so_str in cac_so:
            so = int(so_str)
            if so % 2 != 0:
                so_le.append(so)

    with open(tep_odd, 'w') as f_odd:
        for i in range(4):
            dong_odd = []
            for j in range(4):
                if i * 4 + j < len(so_le):
                    dong_odd.append(str(so_le[i * 4 + j]))
                else:
                    dong_odd.append('0')
            f_odd.write(' '.join(dong_odd) + '\n')
    print("\nNội dung cuối cùng của file ODD.txt:")
    with open(tep_odd, 'r') as f_odd:
        for dong in f_odd:
            print(dong.strip())
ten_tep_du_lieu = 'KHDL18A1HN_16/baitapthuchanhlab11/bai6/data.txt'
ten_tep_odd ='KHDL18A1HN_16/baitapthuchanhlab11/bai6/ODD.txt'
xu_ly_bang_so_khong_try(ten_tep_du_lieu, ten_tep_odd)