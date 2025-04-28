import random
def hoan_vi(A,kq):
    if len(A)==0:
        return 
    i=random.randint(0,len(A)-1)
    so=A[i]
    kq.append(so)
    A.pop(i)
    hoan_vi(A,kq)

n=int(input("Nhap n: "))
A=list(range(1,n+1))
kq=[]
hoan_vi(A,kq)
print(kq)