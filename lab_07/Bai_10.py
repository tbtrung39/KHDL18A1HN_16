
m = input("Nhap so tu nhien m: ")
n = input("Nhap so tu nhien n: ")
chu_so_m = set(m)
chu_so_n = set(n)
chu_so_chung = chu_so_m & chu_so_n
tong = sum(int(chu_so) for chu_so in chu_so_chung)
print("Tong cac chu so chung la:", tong)
