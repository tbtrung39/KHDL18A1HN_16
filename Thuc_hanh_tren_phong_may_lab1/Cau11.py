# 11

def tinh_xac_suat(n):
    p_khong_co_lan_nao = (215/216) ** n
    p_it_nhat_mot_lan = 1 - p_khong_co_lan_nao
    print(f"Xác suất có ít nhất một lần cả 3 viên ra 6 trong {n} lần tung là: {round(p_it_nhat_mot_lan, 2)}")

# Nhập số lần tung
n = int(input("Nhập số lần tung xúc xắc: "))

# Tính xác suất
xac_suat = tinh_xac_suat(n)