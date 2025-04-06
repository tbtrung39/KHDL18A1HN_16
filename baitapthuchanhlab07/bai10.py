m_str= input("Nhập số tự nhiên m: ")
n_str = input("Nhập số tự nhiên n: ")
if m_str.isdigit() and n_str.isdigit():
    m = m_str
    n = n_str
    chu_so_chung = set(m) & set(n)
    tong_chu_so_chung = sum(int(digit) for digit in chu_so_chung)
    print("Các chữ số chung của m và n:", chu_so_chung)
    print("Tổng các chữ số chung:", tong_chu_so_chung)
else:
    print("Vui lòng nhập hai số tự nhiên hợp lệ.")