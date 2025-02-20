import math

n = int(input("Nhập số lần tung xúc sắc: "))

xac_suat_ra_666 = 1 / (6 * 6 * 6)  
xac_suat_khong_ra_666 = 1 - xac_suat_ra_666  

xac_suat_it_nhat_1_lan = 1 - (xac_suat_khong_ra_666 ** n)  

print("Xác suất có ít nhất 1 lần cả 3 xúc sắc ra 6 là:", xac_suat_it_nhat_1_lan)

