nhiphan = input("Nhập chuỗi nhị phân: ")
thapphan = 0
for i in range(len(nhiphan)):
    thapphan = thapphan * 2 + int(nhiphan[i])
print("Số thập phân là:", thapphan)
