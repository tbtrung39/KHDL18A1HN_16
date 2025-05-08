def giai_thua_kep(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua_kep(n - 2)
n = 7
print(f"{n}!! =", giai_thua_kep(n))
