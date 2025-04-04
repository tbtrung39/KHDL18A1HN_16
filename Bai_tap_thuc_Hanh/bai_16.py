n = int(input("Nhập số lượng phần tử n: "))
a = [int(input(f"Nhập a[{i}]: ")) for i in range(n)]

cap_chi_so = []

for i in range(n - 1): 
    for j in range(i + 1, n):  
        if a[i] < a[j]:  
            cap_chi_so.append((i + 1, j + 1))  
print("Các cặp chỉ số thỏa mãn điều kiện:")
for cap in cap_chi_so:
    print(cap)