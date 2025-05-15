# Đọc số nguyên từ tệp m_num.txt
with open("thuc_hanh_tai_phong_may/m_num.txt", "r") as f1:
    data1 = f1.read()
    ds1 = list(map(int, data1.split()))

# Đọc số nguyên từ tệp n_num.txt
with open("thuc_hanh_tai_phong_may/n_num.txt", "r") as f2:
    data2 = f2.read()
    ds2 = list(map(int, data2.split()))

# Tìm các số chung (dùng set để loại trùng)
tap1 = set(ds1)
tap2 = set(ds2)

so_chung = sorted(tap1.intersection(tap2))  # Danh sách các số chung theo thứ tự tăng dần

# Ghi kết quả vào so_chung.txt
with open("so_chung.txt", "w") as fout:
    fout.write(" ".join(map(str, so_chung)))

# In nội dung tệp so_chung.txt ra màn hình
with open("so_chung.txt", "r") as fin:
    noi_dung = fin.read()
    print("Các số có trong cả hai tệp:")
    print(noi_dung)