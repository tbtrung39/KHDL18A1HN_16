chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]  
so = input("Nhập số thập phân: ")  
i = 0  
ket_qua = ""  
while i < len(so):  
    if so[i] == ".":  
        ket_qua += ""  
    else:  
        ket_qua += chu_so[int(so[i])] + " "  
    i += 1  
print("Dạng ký tự:", ket_qua.strip())