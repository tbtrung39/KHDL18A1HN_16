S1= input("Nhập chuỗi S1:")
S2= input("Nhập chuỗi S2:")
m,n = len(S1),len(S2)
dp = [[0]*(n + 1) for _ in range(m+1)]
max_length=0
end_length=0
for i in range (1,m+1):
    for j in range(1,n+1):
        if S1[i-1] == S2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
            if dp[i][j] > max_length:
                max_length = dp[i][j]
                end_index=i
longest_substring= S1[end_index-max_length:end_index]
print("chuỗi con chung dài nhất:",longest_substring)