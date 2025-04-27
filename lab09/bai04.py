def hoan_vi(arr , l , r):
    if l == r:
        print(arr)
    else:
        for i in range( l , r + 1):
            arr[l],arr[i] = arr[i],arr[l]
            hoan_vi(arr, l+1, r)
            arr[l],arr[i] = arr[i],arr[l]

n = int(input("Nhập số:"))
arr = list(range(1, n+1))
print(f"Tất cả hoán vị của dãy [1,2,...{n} là : ")
hoan_vi(arr, 0, n-1)