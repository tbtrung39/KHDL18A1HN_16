a = int(input("a = "))
b = int(input("b = "))
tap_a = {x for x in range(1, a+1) if a % x == 0}
tap_b = {x for x in range(1, b+1) if b % x == 0}
print("Ước chung:", tap_a & tap_b)
