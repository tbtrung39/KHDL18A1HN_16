count = sum(1 for _ in range(10000) if all(random.randint(1, 6) == 6 for _ in range(3)))
print(f"Xác suất: {count / 10000:.2f}")
