n = int(input("Nhập số phần tử: "))
lst = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]

so_le = list(filter(lambda x: x % 2 == 1, lst))
bp_le = list(map(lambda x: x**2, so_le))

print("Bình phương các số lẻ:", bp_le)