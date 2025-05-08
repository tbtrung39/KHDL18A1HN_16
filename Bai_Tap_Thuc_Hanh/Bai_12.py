def tim_ga_cho(ga=0, cho=0):
    if ga + cho > 36:
        return None
    if ga + cho == 36 and ga * 2 + cho * 4 == 100:
        return ga, cho
    ket_qua = tim_ga_cho(ga + 1, cho)
    if ket_qua:
        return ket_qua
    return tim_ga_cho(ga, cho + 1)
kq = tim_ga_cho()
if kq:
    print(f"Số gà: {kq[0]}, Số chó: {kq[1]}")
else:
    print("Không tìm được kết quả phù hợp.")
