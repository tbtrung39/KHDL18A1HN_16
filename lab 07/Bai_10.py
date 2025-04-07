m = int(input("Nhập số m: "))
n = int(input("Nhập số n: "))
chu_so_m = set(str(m))
chu_so_n = set(str(n))
chu_so_chung = chu_so_m & chu_so_n  
tong = sum(int(chu_so) for chu_so in chu_so_chung)
print("Tổng các chữ số chung là:", tong)