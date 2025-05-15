from functools import reduce
def la_so_chan(x):
    return x % 2 == 0
def tinh_tong(lst):
    return reduce(lambda x, y: x + y, lst)
n = int(input("Nhập số nguyên n: "))
ds = list(range(1, n + 1))
so_chan = list(filter(la_so_chan, ds))
tong_chan = tinh_tong(so_chan) if so_chan else 0
print("Danh sách số chẵn:", so_chan)
print("Tổng các số chẵn từ 1 đến", n, "là:", tong_chan)