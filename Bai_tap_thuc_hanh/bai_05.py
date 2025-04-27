def permutation(lst):
    if len(lst) == 0:
        return [[]]
    result = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i+1:]
        for p in permutation(remLst):
            result.append([m] + p)
    return result

n = int(input("Nhập số nguyên dương n: "))
lst = list(range(1, n + 1))

kq = permutation(lst)
print("Các hoán vị của dãy [1, 2, ..., n]:")
for p in kq:
    print(p)
