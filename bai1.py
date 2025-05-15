tong = 0

with open("dayso.dat", "r") as f:
    dong_so = 1
    for line in f:
        if dong_so % 2 == 1:  # Dòng lẻ
            cac_so = line.split()
            for so in cac_so:
                tong += int(so)
        dong_so += 1

print("Tổng các số ở dòng lẻ là:", tong)


