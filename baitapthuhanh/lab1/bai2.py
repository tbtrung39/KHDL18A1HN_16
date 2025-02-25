t = int(input("Nhập số giây: "))
d = t // 86400
h = (t % 86400) // 3600
m = (t % 3600) // 60
s = t % 60
print(f"{d} ngày, {h} giờ, {m} phút, {s} giây")
