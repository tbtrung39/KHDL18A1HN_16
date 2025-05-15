from functools import reduce

def tong_so_chan(lst):
    so_chan = list(filter(lambda x: x % 2 == 0, lst))
    return reduce(lambda a, b: a + b, so_chan, 0)

n = int(input("Nhập số nguyên dương n: "))
danh_sach = list(range(1, n+1))

tong = tong_so_chan(danh_sach)
print(f"Tổng các số chẵn trong danh sách từ 1 đến {n} là: {tong}")