import random

so_ngau_nhien = [so for so in range(0, 201) if so % 5 == 0 and so % 7 == 0]
ket_qua = random.choice(so_ngau_nhien)
print(ket_qua)