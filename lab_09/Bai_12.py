def tim_ga_cho(ga):
    cho = 36 - ga
    if ga < 0 or cho < 0:
        return None
    if 2 * ga + 4 * cho == 100:
        return ga, cho
    return tim_ga_cho(ga - 1)

ket_qua = tim_ga_cho(36)
if ket_qua:
    print("Số con gà là:", ket_qua[0])
    print("Số con chó là:", ket_qua[1])
else:
    print("Không có đáp án thỏa điều kiện.")