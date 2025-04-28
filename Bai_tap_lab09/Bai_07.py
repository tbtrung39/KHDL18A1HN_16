def find_solutions(n, N, current=[], start=1):
    if n == 1:
        if N >= start:
            return [current + [N]]
        else:
            return []
    solutions = []
    for i in range(start, N + 1):
        solutions += find_solutions(n-1, N-i, current + [i], i)
    return solutions
n = int(input("Nhập số biến n: "))
N = int(input("Nhập tổng N: "))
solutions = find_solutions(n, N)
print(f"Các bộ nghiệm của x1+x2+...+x{n}={N}:")
for sol in solutions:
    print(sol)