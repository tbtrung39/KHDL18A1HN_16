binary_str=input("Nhập số nhị phân:")
decimal_num = 0
power = len(binary_str)-1
for binary_digit in binary_str:
    decimal_num += int(binary_digit)*(2**power)
    power -= 1
print("Số thập phân tưởng ứng là :",decimal_num)