n_str = input("Nhập một số nguyên n: ")
if n_str.isdigit():
    n = int(n_str)
    ket_qua_dict = {}
    for i in range(1, n + 1):
        ket_qua_dict[i] = i * i
    print(ket_qua_dict)
else:
    print("Vui lòng nhập một số nguyên hợp lệ.")