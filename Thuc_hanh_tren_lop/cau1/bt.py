with open('Thuc_hanh_tren_lop\cau1\dayso.dat') as f:
    tong = sum(int(x) for line in f for x in line.split() if int(x) % 2 == 1)
print("Tổng các số lẻ là:", tong)