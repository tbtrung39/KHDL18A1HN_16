def tim_ga_cho(ga):
    cho = 36 - ga
    if ga < 0 or cho < 0:
        return None
    if 2 * ga + 4 * cho == 100:
        return ga, cho
    return tim_ga_cho(ga - 1)

ket_qua = tim_ga_cho(36)
if ket_qua:
    print("So ga:", ket_qua[0])
    print("So cho:", ket_qua[1])
else:
    print("Khong co dap an thoa man dieu kien.")