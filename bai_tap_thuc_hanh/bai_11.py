n = int(input("Nhập số lần tung xúc sắc: "))
p_khong_36 = (35/36)**n
p_it_nhat_mot_36 = 1 - p_khong_36
p_it_nhat_mot_36 = round(p_it_nhat_mot_36, 2)
print(f"Xác suất có ít nhất một lần cả 3 xúc sắc ra số 6 trong {n} lần
tung là: {p_it_nhat_mot_36}")