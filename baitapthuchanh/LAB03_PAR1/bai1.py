n = int(input())
s = 0
for i in range(1, n + 1):
    t = (2 * i + 1) / (2 * i + 3)
    s += t
print(round(s, 3))