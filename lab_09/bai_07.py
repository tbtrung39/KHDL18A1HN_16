
def tim_bo_nghiem(N, n, bo_nghiem, start=1):
    if n == 1:
        bo_nghiem.append(bo_nghiem + [N])
        return
    
    for i in range(start, N - n + 2):  
        tim_bo_nghiem(N - i, n - 1, bo_nghiem, i) 
def tim_tat_ca_bo_nghiem(N, n):
    bo_nghiem = []
    tim_bo_nghiem(N, n, bo_nghiem)
    return bo_nghiem
N = int(input("Nhập số tự nhiên N: "))
n = int(input("Nhập số tự nhiên n: "))
bo_nghiem = tim_tat_ca_bo_nghiem(N, n)
print(f"Tất cả các bộ nghiệm của phương trình {N} = x1 + x2 + ... + xn là:")
for bn in bo_nghiem:
    print(bn)
