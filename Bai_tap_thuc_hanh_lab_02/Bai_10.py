h_start = int(input("Nhập h bắt đầu: "))
h_end = int(input("Nhập h kết thúc: "))
tien_san = 0
if 5 <= h_start <= h_end <= 22:
    if  h_start >= 5 and h_end <= 8:
        tien_san = (h_end - h_start)*100000
        print(f"Tiền sân bắt đầu từ {h_start}h đến {h_end}h là: ",tien_san)
    elif 5 <= h_start <= 8 <= h_end < 11:
        tien_san = (8 - h_start)*100000 + (h_end - 8)*(100000 - 0.25*100000)
        print(f"Tiền sân bắt đầu từ {h_start}h đến {h_end}h là: {tien_san}")
    elif 11 <= h_start and h_end <= 15:
        tien_san = (15 - h_start)*(100000 - 0.35*100000) 
        print(f"Tiền sân bắt đầu từ {h_start}h đến {h_end}h là: {tien_san}")
    elif 11 <= h_start <= 15 <= h_end <= 22:
        tien_san = (15 - h_start)*(100000 - 0.35*100000) + (h_end - 15)*(100000 - 0.25*100000)
        print(f"Tiền sân bắt đầu từ {h_start}h đến {h_end}h là: {tien_san}")
else:
    if h_start < 5 :
        print("Sân chưa mở cửa")
    elif h_end > 22:
        print("Sân đã đóng cửa")