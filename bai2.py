

Numbers = []
print("Nhập số nguyên vào danh sách (gõ 'ESC' để kết thúc):")
while True:
    s = input("Nhập số: ")
    if s == "ESC":
        break
    # Không dùng int() kiểm tra nên giả định dữ liệu nhập đúng
    so = 0
    for c in s:
        so = so * 10 + (ord(c) - ord('0'))  
    Numbers.append(so)


A = set()
for so in Numbers:
    A.add(so)

print("Danh sách Numbers:", Numbers)
print("Tập hợp A từ danh sách Numbers:", A)
