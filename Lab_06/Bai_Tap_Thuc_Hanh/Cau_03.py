numbers = []
while True :
    num = int(input("NHập số(nhập 0 đẻ dừng):"))
    if num == 0 :
        break
    numbers.append(num)
print("Danh sách ban đầu :", numbers)
positives = [ x for x in numbers if x > 0]
negatives = [ x for x in numbers if x <= 0]
numbers = positives + negatives
print("Danh sách sau khi đưa số dương len đầu:",numbers)
m = int(input("Nhập số m để chèn vào danh sách:"))
numbers.insert(0,m)
numbers.append(m)
if len(numbers)>=5:
    numbers.insert(4,m)
print("Danh sách sau khi chèn số m:",numbers)