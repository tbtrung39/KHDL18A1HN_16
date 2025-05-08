import random

def sinh_hoan_vi_ngau_nhien(a, ket_qua):
    if not a:
        print("Hoán vị ngẫu nhiên:", ket_qua)
        return
    i = random.randint(0, len(a) - 1)
    phan_tu = a[i]
    sinh_hoan_vi_ngau_nhien(a[:i] + a[i+1:], ket_qua + [phan_tu])
def main():
    n = int(input("Nhập n: "))
    day = list(range(1, n + 1))
    sinh_hoan_vi_ngau_nhien(day, [])

main()
