def sum_a(n):
    if n == 1:
        return 1/2
    return 1/(n*(n+1)) + sum_a(n-1)
n = int(input("Nhập n (bài 8a): "))
print("Tổng S =", sum_a(n))
#B
def factorial(k):
    if k == 1:
        return 1
    return k * factorial(k-1)
def sum_b(n):
    if n == 1:
        return 1
    return 1/factorial(n) + sum_b(n-1)
n = int(input("Nhập n (bài 8b): "))
print("Tổng S =", sum_b(n))
#C
import math
def sum_c(k, n):
    if k == 1:
        return math.sqrt(3)
    return math.sqrt(3*k + sum_c(k-1, n))
n = int(input("Nhập n (bài 8c): "))
print("Tổng S =", sum_c(n, n))
#D
import math
def sum_d(n):
    if n == 1:
        return math.sqrt(1)
    return math.sqrt(n + sum_d(n-1))
n = int(input("Nhập n (bài 8d): "))
print("Tổng S =", sum_d(n))