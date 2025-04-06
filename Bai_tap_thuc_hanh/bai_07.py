import random
A = set([random.randint(0,100) for i in range(10)])
B = set([random.randint(0,100) for i in range(10)])
print("A =", A)
print("B =", B)
print("Các phần tử chung của A, B là:", A & B)