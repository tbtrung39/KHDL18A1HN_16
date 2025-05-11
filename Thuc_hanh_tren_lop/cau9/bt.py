# Đọc dữ liệu từ file PASSENGERS.IN
with open(r"Thuc_hanh_tren_lop\cau9\PASSENGERS.IN", "r") as f:
    lines = f.readlines()

n = int(lines[0])
passengers = [list(map(float, line.split())) for line in lines[1:]]

# Mở các file xuất
with open("WEIGHT.OUT", "w") as fout, open("CANCELED.OUT", "w") as fcancel:
    for idx, items in enumerate(passengers, 1):
        total = sum(items)
        count = len(items)
        fout.write(f"{total:.2f}\n")
        if total > 23 or count > 5:
            fcancel.write(f"{idx}\n")
            # In thông báo cụ thể
            if total > 23:
                print(f"Hành khách số {idx} bị hủy chuyến: quá trọng lượng ({total:.2f} kg)")
            if count > 5:
                print(f"Hành khách số {idx} bị hủy chuyến: quá số kiện ({count} kiện)")