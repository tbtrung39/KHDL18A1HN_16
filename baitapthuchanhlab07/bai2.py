numbers_list = []
print("Nhập các số tự nhiên (nhấn Enter sau mỗi số, nhập 'STOP' để dừng):")
while True:
    num_str = input()
    if num_str == 'STOP':
        break
    if num_str.isdigit():
        numbers_list.append(int(num_str))
    elif num_str:
        print("Vui lòng nhập số tự nhiên.")
print("Danh sách Numbers:", numbers_list)
tap_hop_a = set(numbers_list)
print("Tập hợp A:", tap_hop_a)
