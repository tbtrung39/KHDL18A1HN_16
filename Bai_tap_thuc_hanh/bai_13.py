A = input("Nhập chuỗi A: ")
B = input("Nhập chuỗi B: ")
tim_thay = False
for i in range(1, len(A)): 
    C = A[:i]
    D = A[i:]
    if int(C) + int(D) == int(B):
        print(C + " + " + D + " = " + B)
        tim_thay = True
        break
if not tim_thay:
    print("Không tồn tại cách đặt!")
