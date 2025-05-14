# Bạn có thể bỏ phần này nếu đã có sẵn file dữ liệu
with open("m_num.txt", "w") as f:
    f.write("1 3 5 7 9 11 13 15\n")

with open("n_num.txt", "w") as f:
    f.write("2 3 5 7 10 11 14\n")
# Đọc m số
with open("m_num.txt", "r") as f:
    m_nums = set(map(int, f.read().split()))

# Đọc n số
with open("n_num.txt", "r") as f:
    n_nums = set(map(int, f.read().split()))

# Tìm giao nhau
common_nums = sorted(m_nums & n_nums)

# Ghi ra file so_chung.txt
with open("so_chung.txt", "w") as f:
    f.write(" ".join(map(str, common_nums)))
print("Các số chung là:")
with open("so_chung.txt", "r") as f:
    print(f.read())
