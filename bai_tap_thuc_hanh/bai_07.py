def find_combinations(n, total, current=[]):
    if n == 1:
        current.append(total)
        print(current)
        current.pop()
    else:
        for i in range(total + 1):
            current.append(i)
            find_combinations(n - 1, total - i, current)
            current.pop()

n = int(input("Nhập số lượng biến n: "))
N = int(input("Nhập tổng N: "))
find_combinations(n, N)