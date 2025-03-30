List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
i = 0
while i < 7:  
    print(List_[i])
    i += 1
print("Phần tử thứ hai của sublist thứ 3:", List_[2][1])
count = 0
for _ in List_:
    count += 1
print("Độ dài của List_:", count)
List_.append(["extra", 99])
print("List_ sau khi thêm sublist:", List_)
tong_sale = List_[1][1] + List_[2][1] + List_[5][1] + List_[6][1]
print("Tổng sale value các ngày thứ hai, thứ ba, thứ bảy và chủ nhật:", tong_sale)