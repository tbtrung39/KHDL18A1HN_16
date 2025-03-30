dữ_liệu_nhập = input("Nhập dữ liệu tuple (name, age, score): ")
name = ""
age_chuoi = ""
score_chuoi = ""
chế_độ = 0  # 0: name, 1: age, 2: score
các_chữ_số = "0123456789"
for ký_tự in dữ_liệu_nhập:
    if ký_tự == ',':
        chế_độ += 1
        continue
    if chế_độ == 0:
        name += ký_tự
    elif chế_độ == 1:
        if ký_tự in các_chữ_số:
            age_chuoi += ký_tự
    elif chế_độ == 2:
        if ký_tự in các_chữ_số:
            score_chuoi += ký_tự
age = int(age_chuoi)
score = int(score_chuoi)
tuple_gốc = (name, age, score)
tuple_sắp_xếp = sorted([tuple_gốc], key=lambda x: (x[0], x[1], x[2]))
print(tuple_sắp_xếp[0])