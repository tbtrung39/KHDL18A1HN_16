def tim_ga_cho(ga=0, cho=0):
    if ga + cho > 36:
        return None
    if ga + cho == 36 and 2 * ga + 4 * cho == 100:
        return ga, cho
    ket_qua = tim_ga_cho(ga + 1, cho)
    if ket_qua:
        return ket_qua
    return tim_ga_cho(ga, cho + 1)

ket_qua = tim_ga_cho()
if ket_qua:
    print(f"Số gà: {ket_qua[0]}, Số chó: {ket_qua[1]}")
else:
    print("Không tìm được đáp án phù hợp.")
