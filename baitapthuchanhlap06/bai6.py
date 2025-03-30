danh_sach = list(range(1, 100000, 100))  
danh_sach_tang_dan = sorted(danh_sach)
print("Danh sách tăng dần (10 phần tử đầu):", danh_sach_tang_dan[:10])
danh_sach = list(range(1, 100000, 100)) 
count = 0
for _ in danh_sach:
    count += 1
for i in range(count):
    for j in range(0, count - i - 1):
        if danh_sach[j] > danh_sach[j + 1]:
            danh_sach[j], danh_sach[j + 1] = danh_sach[j + 1], danh_sach[j]
print("Danh sách tăng dần (10 phần tử đầu):", danh_sach[:10])