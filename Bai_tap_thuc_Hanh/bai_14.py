tu_dien_nhi_phan = {i: bin(i)[2:] for i in range(1, 101)}

for k, v in tu_dien_nhi_phan.items():
    print(f"{k}: '{v}'")