W = input("Nhập chuỗi ký tự: ")

tu_dien = {}

for i in range(len(W)):  
    for j in range(i + 1, len(W) + 1):  
        chuoi_con = W[i:j]  
        if chuoi_con in tu_dien:
            tu_dien[chuoi_con] += 1  
        else:
            tu_dien[chuoi_con] = 1  
print("Từ điển các chuỗi con và số lần xuất hiện:")
for k, v in tu_dien.items():
    print(f"'{k}': {v}")