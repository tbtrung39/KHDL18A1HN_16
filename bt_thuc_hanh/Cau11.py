# Câu 11
pi_666 = (1/6)**3

n = int(input("So lan tung: "))
p_khong_666 = (1 - pi_666)**n
p_666_it_nhat_1_lan = round((1 - p_khong_666) * 100, 2)

print(f"Xac suat co it nhat 1 lan ca 3 xuc sac deu ra 6 khi tung {n} lan la: {p_666_it_nhat_1_lan}%")
