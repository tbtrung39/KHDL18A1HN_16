n = int(input("Nhập số lần tung xúc xắc: ")) 
xac_suat_ra_6 = (1/6) ** 3

xac_suat_khong_ra = (1 - xac_suat_ra_6) ** n
xac_suat_it_nhat_1_lan = round(1 - xac_suat_khong_ra, 2) 
     
print(f"\nXác suất có ít nhất 1 lần cả 3 xúc xắc ra 6:{xac_suat_it_nhat_1_lan}")