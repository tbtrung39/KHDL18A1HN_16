so_chu = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
num = input("Nhập một số: ")
i = 0
ket_qua = ""
while i < len(num):
    ket_qua += so_chu[int(num[i])] + " "
    i += 1
print("Số đọc là:", ket_qua.strip())