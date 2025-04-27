def tim_gac(so_con, so_chan, g=0, c=0):
    if g + c == so_con:
        if 2 * g + 4 * c == so_chan:
            return g, c
        else:
            return None
    if g < so_con:
        result = tim_gac(so_con, so_chan, g + 1, c)
        if result:
            return result
    if c < so_con:
        result = tim_gac(so_con, so_chan, g, c + 1)
        if result:
            return result
    return None
so_con = 36
so_chan = 100
ket_qua = tim_gac(so_con, so_chan)

if ket_qua:
    g, c = ket_qua
    print(f"Số con gà là: {g}")
    print(f"Số con chó là: {c}")
else:
    print("Không có kết quả hợp lệ.")
