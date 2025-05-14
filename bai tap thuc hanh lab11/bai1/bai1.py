def tong_so_le_trong_file(filename):
    tong_le = 0
    with open(filename, 'r') as f:
        for line in f:
            numbers = line.strip().split()
            for num in numbers:
                if num.isdigit():
                    n = int(num)
                    if n % 2 != 0:
                        tong_le += n
    return tong_le

filename = input("Nhap duong dan den file muon doc noi dung: ")
tong = tong_so_le_trong_file(filename)
print("Tong cac so le trong file la:", tong)