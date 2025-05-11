# Đọc dữ liệu từ file f_in.dat
with open("Thuc_hanh_tren_lop\cau3\f_out.dat", "r") as f:
    data = list(map(int, f.read().split()))
extremes = []
for i in range(1, len(data) - 1):
    if (data[i - 1] < data[i] > data[i + 1]) or (data[i - 1] > data[i] < data[i + 1]):
        extremes.append(data[i])
with open("Thuc_hanh_tren_lop\cau3\f_out.dat", "w") as f:
    f.write(str(len(extremes)) + "\n")
    f.write(" ".join(map(str, extremes)) + "\n")