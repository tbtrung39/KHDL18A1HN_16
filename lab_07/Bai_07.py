import random
n = int(input("Nhap so luong phan tu cho moi tap hop: "))
tap_hop_A = set()
tap_hop_B = set()
for _ in range(n):
    lua_chon = random.randint(0, 2)
    if lua_chon == 0:  
        ky_tu = chr(random.randint(65, 90))  
    elif lua_chon == 1: 
        ky_tu = chr(random.randint(97, 122))  
    else: 
        ky_tu = str(random.randint(0, 9))  
    tap_hop_A.add(ky_tu)
for _ in range(n):
    lua_chon = random.randint(0, 2)
    if lua_chon == 0: 
        ky_tu = chr(random.randint(65, 90))  
    elif lua_chon == 1:  
        ky_tu = chr(random.randint(97, 122))  
    else:  
        ky_tu = str(random.randint(0, 9)) 
    tap_hop_B.add(ky_tu)
phan_tu_chung = tap_hop_A.intersection(tap_hop_B)
print("\nTap hop A:", tap_hop_A)
print("Tap hop B:", tap_hop_B)
print("Cac phan tu chung:", phan_tu_chung)