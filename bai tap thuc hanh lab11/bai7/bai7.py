# Đọc các số nguyên từ file m_num.txt
with open(r"bai_07\m_nums.txt", "r") as f:
    m_numbers = set(map(int, f.read().split()))

# Đọc các số nguyên từ file n_num.txt
with open(r"bai_07\n_nums.txt", "r") as f:
    n_numbers = set(map(int, f.read().split()))

# Tìm các số chung
common_numbers = sorted(m_numbers.intersection(n_numbers))

# Ghi kết quả ra file so_chung.txt
with open("so_chung.txt", "w") as f:
    for num in common_numbers:
        f.write(str(num) + "\n")

# In nội dung file so_chung.txt ra màn hình
with open("so_chung.txt", "r") as f:
    print("Các số chung là:")
    print(f.read())