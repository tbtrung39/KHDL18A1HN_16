
def permutation(n):
    if n == 1:
        return [[1]]
    else:
        prev = permutation(n - 1)
        result = []
        for p in prev:
            for i in range(len(p) + 1):
                new_p = p[:i] + [n] + p[i:]  
                result.append(new_p)
        return result
n = int(input("Nhập số tự nhiên n: "))
kq = permutation(n)
print("Tất cả hoán vị của dãy [1, 2, ..., n]:")
for p in kq:
    print(p)
