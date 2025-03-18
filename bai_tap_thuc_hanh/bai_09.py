Str=input("nhập chuỗi ký tự:")
max_sub=""
cur_sub= Str[0] if Str else ""
for i in range(1,len(Str)):
    if Str[i] == Str[i-1]:
        cur_sub += Str[i]
    else:
        if len(cur_sub) > len(max_sub):
            max_sub = cur_sub
        cur_sub = Str[i]
if len(cur_sub) > len(max_sub):
    max_sub=cur_sub
print("chuỗi con dài nhất:",max_sub)