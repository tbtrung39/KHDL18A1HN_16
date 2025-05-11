# Đọc các số nguyên từ file m_nums.txt và n_nums.txt
with open(r"Thuc_hanh_tren_lop\cau7\m_nums.txt", "r") as f:
    m_nums = set(map(int, f.read().split()))

with open(r"Thuc_hanh_tren_lop\cau7\n_nums.txt", "r") as f:
    n_nums = set(map(int, f.read().split()))

# Tìm các số chung
common_nums = m_nums.intersection(n_nums)

# Ghi kết quả vào file so_chung.txt
with open("so_chung.txt", "w") as f:
    f.write(" ".join(map(str, sorted(common_nums))) + "\n")

# In nội dung file so_chung.txt ra màn hình
with open("so_chung.txt", "r") as f:
    print(f.read())