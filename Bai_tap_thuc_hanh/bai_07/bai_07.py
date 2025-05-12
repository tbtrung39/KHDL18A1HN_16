def doc_file_so_nguyen(ten_file):
    with open(ten_file, 'r') as f:
        data = f.read()
    return list(map(int, data.strip().split()))

def ghi_file(ten_file, ds):
    with open(ten_file, 'w') as f:
        f.write(' '.join(map(str, ds)))

def in_file(ten_file):
    with open(ten_file, 'r') as f:
        print(f.read())

# Đọc dữ liệu từ 2 file
m_list = doc_file_so_nguyen('m_num.txt')
n_list = doc_file_so_nguyen('n_num.txt')

# Tìm các số chung
so_chung = sorted(set(m_list).intersection(set(n_list)))

# Ghi kết quả vào file
ghi_file('so_chung.txt', so_chung)

# In nội dung file ra màn hình
print("Các số có mặt ở cả hai file là:")
in_file('so_chung.txt')
