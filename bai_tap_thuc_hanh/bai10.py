m = input("Nhập số m: ")
n = input("Nhập số n: ")

tap_m = set()
tap_n = set()

for ch in m:
    if ch.isdigit():
        tap_m.add(ch)

for ch in n:
    if ch.isdigit():
        tap_n.add(ch)

chung = tap_m & tap_n

tong = 0
for ch in chung:
    tong += int(ch)

print("Tổng các chữ số chung:", tong)