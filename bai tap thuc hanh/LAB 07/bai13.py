W = "ahahahahahaha"
tu_dien_chuoi_con = {}
for do_dai in range(1, len(W) + 1):
    for i in range(len(W) - do_dai + 1):
        chuoi_con = W[i:i+do_dai]
        if chuoi_con in tu_dien_chuoi_con:
            tu_dien_chuoi_con[chuoi_con] += 1
        else:
            tu_dien_chuoi_con[chuoi_con] = 1
for chuoi_con, so_lan in tu_dien_chuoi_con.items():
    print(f"({chuoi_con}, {so_lan})")