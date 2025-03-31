import random
danh_sach = []
for i in range(1000):
    danh_sach.append(random.randint(1, 99999))
print("Danh sách ban đầu (10 phần tử đầu):", danh_sach[:10])

# Cách 1: Dùng SSorted()
danh_sach_sap_xep_1 = sorted(danh_sach)
print("Danh sách sau khi sắp xếp (cách 1):", danh_sach_sap_xep_1[:10])

# Cách 2: Không dùng hàm Sororted()
danh_sach_sap_xep_2 = danh_sach[:]
for i in range(len(danh_sach_sap_xep_2) - 1):
    for j in range(len(danh_sach_sap_xep_2) - i - 1):
        if danh_sach_sap_xep_2[j] > danh_sach_sap_xep_2[j + 1]:
            danh_sach_sap_xep_2[j], danh_sach_sap_xep_2[j + 1] = danh_sach_sap_xep_2[j + 1], danh_sach_sap_xep_2[j]
print("Danh sách sau khi sắp xếp (cách 2):", danh_sach_sap_xep_2[:10])