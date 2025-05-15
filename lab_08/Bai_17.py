from functools import reduce

n = int(input("Nhập số nguyên dương n: "))

ds = list(range(1, n + 1))

so_chan = list(filter(lambda x: x % 2 == 0, ds))

tong_chan = reduce(lambda x, y: x + y, so_chan)

print("Danh sách số nguyên từ 1 đến", n, "là:", ds)
print("Các số chẵn:", so_chan)
print("Tổng các số chẵn:", tong_chan)
