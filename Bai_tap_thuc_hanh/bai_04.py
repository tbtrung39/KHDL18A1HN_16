def hoan_vi(arr, l, r):
    if l == r:
        print(arr)
    else:
        for i in range(l, r + 1):
            arr[l], arr[i] = arr[i], arr[l]  
            hoan_vi(arr, l + 1, r)        
            arr[l], arr[i] = arr[i], arr[l]  

n = int(input("Nhập số tự nhiên n: "))
day_so = [i for i in range(1, n + 1)]

print(f"Tất cả hoán vị của dãy từ 1 đến {n} là:")
hoan_vi(day_so, 0, n - 1)