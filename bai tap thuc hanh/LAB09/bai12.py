def tim_ga_cho(ga=0, cho=0):
    if ga + cho > 36:
        return None
    if ga + cho == 36 and (ga * 2 + cho * 4) == 100:
        return (ga, cho)
    ket_qua = tim_ga_cho(ga, cho + 1)
    if ket_qua:
        return ket_qua
    return tim_ga_cho(ga + 1, 0)

ket_qua = tim_ga_cho()
if ket_qua:
    print("Số con gà là:", ket_qua[0])
    print("Số con chó là:", ket_qua[1])
else:
    print("Không tìm thấy kết quả.")