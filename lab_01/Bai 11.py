import random
so_lan_thu = 100000
dem = 0
for i in range(so_lan_thu):
    xuc_xac_1 = random.randint(1, 6)
    xuc_xac_2 = random.randint(1, 6)
    xuc_xac_3 = random.randint(1, 6)
    if 6 in [xuc_xac_1, xuc_xac_2, xuc_xac_3]:
        dem += 1
xac_suat = dem / so_lan_thu
print(f"Xac suat gieo 3 xuc xac co it nhat 1 lan ra 6: {xac_suat:.2f}")