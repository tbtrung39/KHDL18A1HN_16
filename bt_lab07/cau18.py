thong_tin_thi_sinh={}
while True:
    so_bao_danh = input("Nhập Số báo danh (hoặc 'stop' để dừng): ")
    if so_bao_danh.lower() == 'stop':
        break
    if so_bao_danh in thong_tin_thi_sinh:
        print("Thông tin thí sinh có SBD", so_bao_danh + ":")
        print("Họ tên:", thong_tin_thi_sinh[so_bao_danh]['ho_ten'])
        print("Điểm thi:", thong_tin_thi_sinh[so_bao_danh]['diem_thi'])
    else:
        print("Không tìm thấy thí sinh có SBD", so_bao_danh + ".")
        them_moi = input("Bạn có muốn thêm thông tin cho SBD này (y/n)? ")
        if them_moi.lower() == 'y':
            ho_ten_moi = input("Nhập Họ và tên: ")
            diem_thi_moi_str = input("Nhập Điểm thi: ")
            if diem_thi_moi_str.isdigit():
                diem_thi_moi = int(diem_thi_moi_str)
                thong_tin_thi_sinh[so_bao_danh] = {'ho_ten': ho_ten_moi, 'diem_thi': diem_thi_moi}
                print("Đã thêm thông tin cho SBD", so_bao_danh + ".")
            else:
                print("Điểm thi phải là số nguyên.")