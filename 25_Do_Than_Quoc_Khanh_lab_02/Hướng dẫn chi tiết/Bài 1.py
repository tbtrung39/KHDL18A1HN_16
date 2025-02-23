                #Hướng dẫn bài tập
#Bài 1: Kiểm tra năm nhuận
print("Chương trình kiểm tra năm nhuận")
print("Nhập năm cần kiểm tra:",end="")
nam=int(input())
if (nam%4==0 and nam % 100 != 0) or nam %400==0:
    print("Năm",nam,"là năm nhuận!")
else:
    print("Năm",nam,"không là năm nhuận!")