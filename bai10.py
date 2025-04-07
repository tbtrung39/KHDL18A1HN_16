# Bài 10: Nhập số nguyên dương, đếm chữ số xuất hiện nhiều nhất

n = int(input("Nhập số nguyên dương: "))

tan_so = {}
while n > 0:
    cs = n % 10
    if cs in tan_so:
        tan_so[cs] += 1
    else:
        tan_so[cs] = 1
    n = n // 10

# Tìm chữ số xuất hiện nhiều nhất
max_lan = 0
cs_max = []

for k in tan_so:
    if tan_so[k] > max_lan:
        max_lan = tan_so[k]

for k in tan_so:
    if tan_so[k] == max_lan:
        cs_max.append(k)

print("Chữ số xuất hiện nhiều nhất là:")
for x in cs_max:
    print(x, "xuất hiện", max_lan, "lần")
