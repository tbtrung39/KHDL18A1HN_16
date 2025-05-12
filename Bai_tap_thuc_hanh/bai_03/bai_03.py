def is_extreme(arr, i):
    # Kiểm tra điều kiện cực trị
    return (arr[i-1] < arr[i] > arr[i+1]) or (arr[i-1] > arr[i] < arr[i+1])

def find_extremes(input_file, output_file):
    with open(input_file, 'r') as f:
        arr = list(map(int, f.read().split()))

    extremes = []
    for i in range(1, len(arr) - 1):
        if is_extreme(arr, i):
            extremes.append(arr[i])

    with open(output_file, 'w') as f:
        f.write(f"{len(extremes)}\n")
        f.write(" ".join(map(str, extremes)))

# Gọi hàm với file vào/ra
find_extremes("f_in.dat", "f_out.dat")
