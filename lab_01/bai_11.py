so_lan_tung = int(input("Nhập số lần tung xúc xắc: "))
tong_truong_hop = 6 ** (3 * so_lan_tung)  
truong_hop_sai = 4 ** (3 * so_lan_tung)  
xac_suat = (tong_truong_hop - truong_hop_sai) / tong_truong_hop  
ket_qua = round(xac_suat, 2)
print(f"Xác suất có ít nhất một lần cả 3 và 6 xuất hiện trong {so_lan_tung} lần tung là: {ket_qua}")
