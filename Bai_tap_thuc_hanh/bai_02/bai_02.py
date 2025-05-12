with open("Bai_tap_thuc_hanh\Inp.txt", "r") as f:
    line = f.readline()
    numbers = list(map(int, line.strip().split()))

numbers.sort()

with open("Bai_tap_thuc_hanh\out.dat", "w") as f:
    for num in numbers:
        f.write(str(num) + " ")
