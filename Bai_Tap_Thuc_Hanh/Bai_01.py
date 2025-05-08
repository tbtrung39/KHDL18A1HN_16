def max_hai_so(x,y):
    if x < y:
        return y
    else:
        return x
def ktr_3_so(a, b, c):
    return max_hai_so(max_hai_so(a,b),c)
a,b,c = map(int,input("Nhập 3 số a,b,c: ").split())
print(ktr_3_so(a,b,c))