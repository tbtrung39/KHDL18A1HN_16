with open("f_in.dat", "r") as f:
    arr = list(map(int, f.read().split()))

extremes = []
for i in range(1, len(arr) - 1):
    if (arr[i-1] < arr[i] > arr[i+1]) or (arr[i-1] > arr[i] < arr[i+1]):
        extremes.append(arr[i])

with open("f_out.dat", "w") as f:
    f.write(str(len(extremes)) + "\n")
    f.write(" ".join(map(str, extremes)))
