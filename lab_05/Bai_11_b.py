chuoi_nhi_phan = input("Nhập chuỗi nhị phân: ")

so_thap_phan = 0
luy_thua = 1  # Giá trị 2^0 = 1

for i in range(len(chuoi_nhi_phan) - 1, -1, -1):  # Duyệt từ cuối chuỗi về đầu
    if chuoi_nhi_phan[i] == '1':  # Nếu là bit 1 thì cộng vào tổng
        so_thap_phan += luy_thua
    luy_thua *= 2  # Nhân lũy thừa lên 2 mỗi bước

print("Giá trị thập phân:", so_thap_phan)