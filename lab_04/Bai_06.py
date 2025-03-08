chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]  
so = input("Nhập số: ")  
i = 0  
ket_qua = ""  

while i < len(so):  
    chu_ky_tu = so[i]  
    ket_qua += chu_so[int(chu_ky_tu)] + " "  
    i += 1  

print("Số bằng chữ:", ket_qua.strip())