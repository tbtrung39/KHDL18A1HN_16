import random
num = random.randint(0, 200)
if num % 5 == 0 and num % 7 == 0:
    print(f"Số {num} chia hết cho cả 5 và 7.")
else:
    print(f"Số {num} không chia hết cho cả 5 và 7.")
