d=int(input('Nhập số ngày:'))
h=int(input('Nhập sô giờ:'))
m=int(input('Nhập sô phút:'))
s=int(input('Nhập số giây:'))
total_second=d*86400+h*3600+m*60+s
print(f"Tổng số giây ứng với {d} ngày {h} giờ {m} phút {s} giây :{total_second} giây")