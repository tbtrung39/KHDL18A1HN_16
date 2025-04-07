w = input("Nhap chuoi W: ")
ket_qua = {}
for do_dai in range(1, len(w) + 1):
    for i in range(len(w) - do_dai + 1):
        k = w[i:i + do_dai]
        if k not in ket_qua:
            ket_qua[k] = w.count(k)
print("Tu dien ket qua:")
for k, v in ket_qua.items():
    print(k, ":", v)
    