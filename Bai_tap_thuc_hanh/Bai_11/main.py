from hinhhoc import my_Triage, my_square

print("=== Tam giác ===")
cv_tg = my_Triage.tinh_chu_vi(3, 4, 5)
dt_tg = my_Triage.tinh_dien_tich(3, 4)
print("Chu vi:", cv_tg)
print("Diện tích:", dt_tg)

print("=== Hình vuông ===")
cv_sq = my_square.tinh_chu_vi(5)
dt_sq = my_square.tinh_dien_tich(5)
print("Chu vi:", cv_sq)
print("Diện tích:", dt_sq)
