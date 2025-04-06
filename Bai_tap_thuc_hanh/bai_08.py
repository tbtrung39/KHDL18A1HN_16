my_set = {1, 2.5, "hello", 3, 4.0, "world", 5}
int_count = 0
float_count = 0
str_count = 0
for item in my_set:
    if type(item) == int:
        int_count += 1
    elif type(item) == float:
        float_count += 1
    elif type(item) == str:
        str_count += 1
print("Số nguyên:", int_count)
print("Số thực:", float_count)
print("Chuỗi:", str_count)