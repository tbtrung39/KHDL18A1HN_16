with open(file="Bài_tập_thực_Hành/dayso.dat", mode="r") as f :
    data = f.read()
numbers = list(map(int, data.split()))
tong_le = sum(x for x in numbers if x % 2 == 1)
print("Tổng các số lẻ trong dãy là :",tong_le)