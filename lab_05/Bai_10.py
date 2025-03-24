# Nhập 2 chuỗi từ bàn phím
Str1 = input("Nhập chuỗi Str1: ")
Str2 = input("Nhập chuỗi Str2: ")

# Cách 1: Dùng Quy hoạch động (Dynamic Programming)
m = len(Str1)
n = len(Str2)
dp = [[0] * (n + 1) for _ in range(m + 1)]  # Bảng DP lưu độ dài LCS
max_length = 0
end_index = 0  # Vị trí kết thúc của chuỗi con chung dài nhất

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if Str1[i - 1] == Str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            if dp[i][j] > max_length:
                max_length = dp[i][j]
                end_index = i  # Lưu vị trí kết thúc của LCS trong Str1

lcs1 = Str1[end_index - max_length:end_index]  # Trích xuất chuỗi con chung
print("Chuỗi con chung dài nhất (cách 1):", lcs1)

# Cách 2: Dùng vòng lặp để kiểm tra từng chuỗi con
max_length2 = 0
lcs2 = ""

for i in range(m):
    for j in range(i, m):  # Lấy từng chuỗi con của Str1
        sub_str = Str1[i:j + 1]
        if sub_str in Str2 and len(sub_str) > max_length2:
            max_length2 = len(sub_str)
            lcs2 = sub_str

print("Chuỗi con chung dài nhất (cách 2):", lcs2)