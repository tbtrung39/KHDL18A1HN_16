def tim_max(a,b,c):
   if a>=b:
        if a>=c:
            return a
        else:
            return c
   else:
       return tim_max(b,c,a)
      
a,b,c=map(int,input("Nhap:").split(" "))
kq=tim_max(a,b,c)
print(kq)