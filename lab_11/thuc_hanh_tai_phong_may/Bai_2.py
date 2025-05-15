# Đọc dữ liệu từ tệp Inp.txt
with open("thuc_hanh_tai_phong_may\Inp.txt", "r") as f:
    dong = f.readline()  # Đọc dòng duy nhất chứa các số

# Tách và chuyển chuỗi sang danh sách số nguyên
ds = list(map(int, dong.split()))

# Sắp xếp tăng dần
ds_sapxep = sorted(ds)

# Ghi kết quả vào tệp out.dat
with open("thuc_hanh_tai_phong_may\out.dat", "w") as f:
    # Ghi các số, ngăn cách bằng dấu cách
    f.write(" ".join(map(str, ds_sapxep)))