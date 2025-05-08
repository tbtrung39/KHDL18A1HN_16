def doc_du_lieu(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    n = int(lines[0].strip())
    hanh_ly = [list(map(float, line.strip().split())) for line in lines[1:]]
    return n, hanh_ly

def xu_ly_du_lieu(n, hanh_ly):
    tong_trong_luong = []
    bi_huy = []

    for i in range(n):
        tong = sum(hanh_ly[i])
        so_mon = len(hanh_ly[i])
        tong_trong_luong.append(tong)
        
        if tong > 23 or so_mon > 5:
            bi_huy.append((i + 1, tong, so_mon))
    
    return tong_trong_luong, bi_huy

def ghi_file_ket_qua(weights, canceled):
    with open("Bài_tập_thực_Hành/WEIGHT.OUT", "w") as f:
        for weight in weights:
            f.write(f"{weight:.2f}\n")

    with open("Bài_tập_thực_Hành/CANCELED.OUT", "w") as f:
        for hanh_khach, _, _ in canceled:
            f.write(f"{hanh_khach}\n")

def in_thong_bao_huy_chuyen(canceled):
    print("\n Danh sách hành khách bị hủy chuyến:")
    for hanh_khach, tong, so_mon in canceled:
        ly_do = []
        if tong > 23:
            ly_do.append(f"tổng trọng lượng {tong:.2f} kg vượt quá 23 kg")
        if so_mon > 5:
            ly_do.append(f"số lượng món {so_mon} vượt quá 5")
        print(f"- Hành khách {hanh_khach}: " + ", ".join(ly_do))

if __name__ == "__main__":
    file_path = "Bài_tập_thực_Hành/PASSENGERS.IN"
    n, hanh_ly = doc_du_lieu(file_path)
    weights, canceled = xu_ly_du_lieu(n, hanh_ly)
    ghi_file_ket_qua(weights, canceled)
    in_thong_bao_huy_chuyen(canceled)