# Câu 13
A = input("Nhập chuỗi A: ")
B = input("Nhập chuỗi B: ")
for i in range(1, len(A)):  
    for j in range(1, len(B)): 
        new_A = A[:i] + '+' + A[i:]
        new_B = B[:j] + '+' + B[j:]
        sum_A = 0
        for part in new_A.split('+'):
            sum_A += int(part)
        sum_B = 0
        for part in new_B.split('+'):
            sum_B += int(part)
        if sum_A == sum_B:
            print("Đẳng thức đúng:",new_A, "=",new_B)
            exit()
print("Không tồn tại cách đặt")