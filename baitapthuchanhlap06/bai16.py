dữ_liệu_nhập = input("Nhập X và Y (cách nhau bởi dấu phẩy): ")
X_chuoi = ""
Y_chuoi = ""
chế_độ = 0  # 0: X, 1: Y
các_chữ_số = "0123456789"
for ký_tự in dữ_liệu_nhập:
    if ký_tự == ',':
        chế_độ += 1
        continue

    if ký_tự in các_chữ_số:
        if chế_độ == 0:
            X_chuoi += ký_tự
        else:
            Y_chuoi += ký_tự
X = int(X_chuoi)
Y = int(Y_chuoi)
mảng = [[i * j for j in range(Y)] for i in range(X)]
print(mảng)