n = int(input("Nhập số nguyên dương :"))
if n <= 0:
    print("Không phải sô nguyên dương")
else:
    print("Phân tích n thành số nguyên tố:" , end="")
    for i in range(2,n+1):
        if n%i ==0:
         print(i , end="")
         n//=i