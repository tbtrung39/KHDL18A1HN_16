from functools import reduce

n = int(input("Nhập số phần tử: "))
lst = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]

so_chan = list(filter(lambda x: x % 2 == 0, lst))
tong_chan = reduce(lambda x, y: x + y, so_chan, 0)

print("Tổng các số chẵn trong danh sách:", tong_chan)
