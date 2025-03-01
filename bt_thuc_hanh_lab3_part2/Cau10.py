# Câu 10
n = int(input("Nhập số nguyên n: "))
while n <= 0:
    n = int(input("Nhập lại số nguyên n (n phải > 0): "))

print("Dạng phân tích:", end=" ")

uoc = 2  
while n > 1:
    while n % uoc == 0:
        print(uoc, end=" ")
        n //= uoc  
    uoc += 1 
