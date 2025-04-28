import random
def tao_hoan_vi(A,result):
    if len(A)==0:
        return
    i=random.randint(0,len(A)-1)
    so=A[i]
    result.append(so)
    A.pop(i)
    tao_hoan_vi(A,result)
n=int(input("Nhap n: "))
A=list(range(1,n+1))
result=[]
tao_hoan_vi(A,result)
print("Hoan vi ngau nhien:",result)