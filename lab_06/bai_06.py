import random
A = [random.randint(1,99999)for _ in range(1000)]
print("Danh sách A ban dầu :",A[:20],"...")
A_sorted_1 = sorted(A)
print("Danh sách A sau khi sắp xếp:",A_sorted_1)
A_sorted_2= A[:]
n = len(A_sorted_2)
for i in range (n - 1):
    for j in range (n-1-i):
        if A_sorted_2[j]>A_sorted_2[j+1]:
            A_sorted_2[j],A_sorted_2[j+1]= A_sorted_2[j+1],A_sorted_2[j]
print("Danh sách a sau khi săp xếp:",A_sorted_2[:20],"...")