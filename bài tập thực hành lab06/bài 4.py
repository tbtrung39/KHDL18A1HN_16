arr =[]
while True:
    num = int(input("Nhập số tự nhiên (Nhập 0 để dừng):"))
    if num == 0:
        break
    arr.append(num)
print("Danh sách ban đầu:",arr)
new_list = [1,2,3]
arr = new_list + arr
arr.extend(new_list)
if len(arr) >= 5:
    arr = arr[:5] + new_list + arr[5:]
print("danh schs sai khi chèn :",arr)
k = int(input("Nhập vị trí cần xóa k(tính từ 0):"))
if 0 <= k < len(arr):
    arr.pop(k)
    print("Danh sách sau khi xóa phần tử thứ",k,":",arr)
else:
    print("Vị trí không hợp lệ")
arr_asc = sorted(arr)
print('Danh sách sắp xếp theo tăng dần:',arr_asc)
arr_desc = sorted(arr,reverse=True)
print('Danh sách sắp xếp theo giamr dần:',arr_desc)