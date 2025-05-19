def UCLN(a, b): 
    while b:
        a, b = b, a % b
    return a

def BCNN(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // UCLN(a, b)

def SumDivisor(n):
    if not isinstance(n, int) or n <= 0:
        return "Lỗi: n phải là một số nguyên dương."
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    return total

if __name__ == "__main__":
    print("Đây là module sohoc. Vui lòng chạy file chương trình chính để sử dụng.")