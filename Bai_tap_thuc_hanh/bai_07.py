def solve(n, N, current=[], result=[]):
    if n == 0:
        if N == 0:
            result.append(current.copy())
        return
    for i in range(N + 1):
        current.append(i)
        solve(n - 1, N - i, current, result)
        current.pop()

n = int(input("Nhập số lượng biến n: "))
N = int(input("Nhập tổng N cần đạt được: "))

result = []
solve(n, N, [], result)

print(f"Các bộ nghiệm (x₁, x₂, ..., xₙ) sao cho tổng bằng {N} là:")
for r in result:
    print(r)
