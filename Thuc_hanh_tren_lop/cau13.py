W = input("Nhập chuỗi ký tự: ")
substrings_dict = {}

for i in range(len(W)):
    for j in range(i+1, len(W)+1):
        substring = W[i:j] 
        if substring in substrings_dict:
            substrings_dict[substring] += 1  
        else:
            substrings_dict[substring] = 1  
print(substrings_dict)