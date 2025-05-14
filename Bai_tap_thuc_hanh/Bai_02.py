with open("Inp.txt", "r") as f:
    numbers = list(map(int, f.read().split()))
    numbers.sort()

with open("out.dat", "w") as f:
    f.write(" ".join(map(str, numbers)))
