from itertools import combinations
A = input("Nhập chuỗi A:")
B=input("Nhập chuỗi B:")
nA=len(A)
nB=len(B)
A_splits=[]
B_splits=[]
for i in range (1,nA):
    C=int(A[:i])
    D=int(A[i:])
    A_splits.append((C,D))
for j in range(1,nB):
    E=int(B[:j])
    F=int(B[j:])
    B_splits.append((E,F))
found = False
for C,D in A_splits:
    for E,F in B_splits:
        if C + D == E + F:
            print(f'{C} + {D} = {E} + {F}')
            found= True
if not found:
    print("Không có cách đặt")