import random
danh_sach_so = list(range(10))
tap_hop_a = set()
while len(tap_hop_a) < 5:
    phan_tu_ngau_nhien = random.choice(danh_sach_so)
    tap_hop_a.add(phan_tu_ngau_nhien)
print("Tập hợp A (5 phần tử ngẫu nhiên):", tap_hop_a)
