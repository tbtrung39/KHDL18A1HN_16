def tong_so_le_trong_file(filename):
    tong = 0
    with open(filename, 'r') as f:
        for line in f:
            numbers = map(int, line.split())
            tong += sum(x for x in numbers if x % 2 == 1)
    return tong

file_path = 'Bai_tap_thuc_hanh\dayso.dat'
tong_le = tong_so_le_trong_file(file_path)
print("Tổng các số lẻ trong file là:", tong_le)
