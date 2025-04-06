binary_dict = {}
i = 1
while i <= 100:
    binary_str = bin(i)[2:]  
    binary_dict[i] = binary_str
    i += 1
print(binary_dict)