def to_hop(N, current, start):
    if N == 0:
        print(current)
        return
    for i in range(start, N+1):
        to_hop(N-i, current + [i], i)

N = int(input("Nhập tổng N: "))
to_hop(N, [], 1)
