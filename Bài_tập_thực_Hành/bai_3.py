with open("Bài_tập_thực_Hành/f_in.dat", "r") as f_in:
    line = f_in.readline()
    numbers = list(map(int, line.strip().split()))

extremes = []
for i in range(1, len(numbers) - 1):
    if (numbers[i - 1] < numbers[i] > numbers[i + 1]) or \
       (numbers[i - 1] > numbers[i] < numbers[i + 1]):
        extremes.append(numbers[i])

with open("Bài_tập_thực_Hành/f_out.dat", "w") as f_out:
    f_out.write(str(len(extremes)) + "\n")
    f_out.write(" ".join(map(str, extremes)))