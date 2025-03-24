str1 = input("Nhập chuỗi ký tự str1: ")
str2 = input("Nhập chuỗi ký tự str2: ")
str = ""
n = len(str1)
n1 = len(str2)
max_len = max(n,n1) # Kiểm tra xem max của 2 chuối đấy làm bao nhiêu đển làm mốc
for i in range(max_len): # cho chạy đến max_len đển test xem chuỗi nào kết thúc trước
    if i < n:
        str = str + str1[i]
    if i < n1:
        str = str + str2[i]
print(str)
