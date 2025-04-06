a_str  = input("Nhập dãy số nguyên a (cách nhau bởi dấu cách): ")
a = [int(x) for x in a_str.split()]
s_str = input("Nhập số cho trước S: ")
if s_str.isdigit():
    s = int(s_str)
    n = len(a)
    cac_cap_chi_so = []
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] + a[j] == s:
                cac_cap_chi_so.append((i, j))
    print("Các cặp chỉ số (i, j) có tổng bằng", s, "là:", cac_cap_chi_so)
else:
    print("Vui lòng nhập một số nguyên hợp lệ cho S.")