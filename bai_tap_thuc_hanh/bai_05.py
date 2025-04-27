def permutation(arr, l, r):
    if l == r:
        print(arr)
    else:
        for i in range(l, r + 1):
            arr[l], arr[i] = arr[i], arr[l]  # Hoán đổi
            permutation(arr, l + 1, r)
            arr[l], arr[i] = arr[i], arr[l]  # Đổi lại để thử trường hợp khác

n = int(input("Nhập n: "))
arr = list(range(1, n + 1))
permutation(arr, 0, n - 1)