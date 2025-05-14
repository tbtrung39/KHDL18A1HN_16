# a.
def sum_a(n):
    if n == 1:
        return 1 / (1 * 2)
    else:
        return 1 / (n * (n + 1)) + sum_a(n - 1)

# b.
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def sum_b(n):
    if n == 1:
        return 1
    else:
        return 1 / factorial(n) + sum_b(n - 1)

# c.
def sum_c(n):
    if n == 1:
        return 3
    else:
        return (3 * n + sum_c(n - 1)) ** 0.5

# d.
def sum_d(n):
    if n == 1:
        return 1
    else:
        return (n + sum_d(n - 1)) ** (1 / (n + 1))
        
n = int(input("Nhập số tự nhiên n: "))
print("Sa:", sum_a(n))
print("Sb:", sum_b(n))
print("Sc:", sum_c(n))
print("Sd:", sum_d(n))