import random
list_ = [
    ["mon",73],
    ["tue",89],
    ["wed",95],
    ["thu",103],
    ["fri",115],
    ["sat",128],
    ["sun",120]
]
print("Danh sách List_:")
for item in list_:
    print(item)
phan_tu=list_[2][1]
print("\n Phần tử thứ hai cảu sublist thứ 3:",phan_tu)
print("\n Đọ dài danh sách trước khi thêm :",len(list_))
random_day=random.choice(["mon","tue","wed","thu","fri","sat","sun"])
random_value = random.randint(50,150)
list_.append([random_day,random_value])
print("\n Danh sách sau khi thêm sublist ngẫu nhiên:")
for item in list_:
    print(item)
    tong=0
    for item in list_:
        if item[0]in["mon","tue","sat","sun"]:
            tong+=item[1]
    print("\n Tổng sale value trong các ngày thứ hai , thứ ba ,thứ bảy ,chủ nhật:",tong)