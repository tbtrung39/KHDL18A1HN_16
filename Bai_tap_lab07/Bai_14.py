binary_dict = {i: bin(i)[2:] for i in range(1, 101)}
print("Dictionary số - nhị phân (10 số đầu):", dict(list(binary_dict.items())[:10]))