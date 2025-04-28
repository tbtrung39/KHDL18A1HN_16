def tim_ga_cho(g=0):
    c = 36 - g  
    if g > 36:
        return None  
    if 2 * g + 4 * c == 100:
        return g, c
    return tim_ga_cho(g + 1)
ket_qua = tim_ga_cho()
if ket_qua:
    ga, cho = ket_qua
    print(f"Số con gà là: {ga}")
    print(f"Số con chó là: {cho}")
else:
    print("Không tìm được nghiệm phù hợp.")