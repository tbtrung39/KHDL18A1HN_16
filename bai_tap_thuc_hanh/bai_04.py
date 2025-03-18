S1= input("Nhập chuỗi S1:")
S2= input("Nhập chuỗi S2:")
result=""
i=0
while i < len(S1) or i < len(S2):
    if i < len(S1):
        result += S1[i]
    if i < len(S2):
        result +=S2[i]
    i +=1
print("Chuỗi sau khi trộn :",result)
