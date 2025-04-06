w = input("Nhập vào chuỗi ký tự W: ")
substring_counts = {}

n = len(w)
for length in range(1, n + 1):  
    for i in range(n - length + 1):  
        sub = ""
        for k in range(i, i + length): 
            sub += w[k]
        substring_counts[sub] = substring_counts.get(sub, 0) + 1

print(substring_counts)