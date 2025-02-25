nam = int(input("Nhập năm cần ktr: "))
if (nam % 4 == 0 and nam % 100 != 0) or nam % 400 == 0:
    print(f"{nam} là năm nhuận")
else:
    print(f"{nam} k phải là năm nhuận") 