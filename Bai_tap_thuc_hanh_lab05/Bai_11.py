n = input("Nhập chuỗi ký tự nhị phân muốn chuyển đổi: ")
ch_doi = 0
for i in range(len(n)):
    ch_doi += int(n[i])*(2**(len(n)-i-1))
print(ch_doi)

