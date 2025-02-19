n = int(input("Nhập số lần tung 3 xúc sắc: "))
xac_suat_khong_ra_666 = 1 - (1 / 216)
xac_suat_khong_co_666 = xac_suat_khong_ra_666 ** n
xac_suat_it_nhat_1_lan_ra_666 = 1 - xac_suat_khong_co_666
print("Xác suất ít nhất 1 lần cả 3 xúc sắc ra 6 sau", n, "lần tung là:", round(xac_suat_it_nhat_1_lan_ra_666, 2))

