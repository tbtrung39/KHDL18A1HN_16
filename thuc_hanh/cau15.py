a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]

tan_suat = {}
for num in a:
    if num in tan_suat:
        tan_suat[num] += 1
    else:
        tan_suat[num] = 1

max_count = 0
max_value = None
for num, count in tan_suat.items():
    if count > max_count:
        max_count = count
        max_value = num
print("Phần tử xuất hiện nhiều nhất là:", max_value, "với", max_count, "lần")
