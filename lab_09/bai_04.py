
def hoan_vi(arr, l, r):
    if l == r:
        print(arr)
    else:
        for i in range(l, r + 1):
            arr[l], arr[i] = arr[i], arr[l]  
            hoan_vi(arr, l + 1, r)          
            arr[l], arr[i] = arr[i], arr[l] 
n = int(input("Nhập số tự nhiên n: "))
day = [i for i in range(1, n + 1)]
hoan_vi(day, 0, n - 1)
