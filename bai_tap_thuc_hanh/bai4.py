heights = [161,182,161,154,176,170,167,171,170,174,150,142,148,165,170,178,156,145,
           149,163,162,159,165,165,170,180,155,159,155,153,152,162,180,168,169,168,167,170]

# a
print("Số sinh viên:", len(heights))

# b
tong = 0
for h in heights:
    tong += h
trung_binh = tong / len(heights)
print("Chiều cao trung bình:", round(trung_binh, 2))

# c
chieu_cao_khac_nhau = []
for h in heights:
    if h not in chieu_cao_khac_nhau:
        chieu_cao_khac_nhau.append(h)
chieu_cao_khac_nhau.sort()
print("Các chiều cao khác nhau:", chieu_cao_khac_nhau)
print("Chiều cao trung bình:", round(trung_binh, 2))