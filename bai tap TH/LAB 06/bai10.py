import random
danh_sach = []
for i in range(100):
    so = random.randint(0, 200)
    if so % 35 == 0:
        danh_sach.append(so)
print("Danh sách số chia hết cho 5 và 7:", danh_sach)