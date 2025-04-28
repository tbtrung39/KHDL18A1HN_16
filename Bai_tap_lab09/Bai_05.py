def permutation(n):
    if n == 1:
        return [[1]]
    else:
        result = []
        for p in permutation(n-1):
            for i in range(len(p)+1):
                new_p = p.copy()
                new_p.insert(i, n)
                result.append(new_p)
        return result
n = int(input("Nhập số n: "))
print(f"Các hoán vị của [1,...,{n}]:")
for p in permutation(n):
    print(p)